import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, x, y, visited, step):
    q = deque([[x, y]])
    visited[y][x] = step
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= k or 0 > ny or ny >= n:
                continue
            if visited[ny][nx] == 0 and graph[ny][nx] != 0:
                visited[ny][nx] = step
                q.append([nx, ny])
    return visited

def melting(graph):
    melting_arr = [[0]* k for _ in range(n)]
    for i in range(k):
        for j in range(n):
            if graph[j][i] != 0:
                for a in range(4):
                    nx = i + dx[a]
                    ny = j + dy[a]
                    if 0 > nx or nx >=k or 0 > ny or ny >= n:
                        continue
                    if graph[ny][nx] == 0:
                        melting_arr[j][i] += 1
    for i in range(k):
        for j in range(n):
            tmp = graph[j][i] - melting_arr[j][i]
            graph[j][i] = tmp if tmp >= 0 else 0
    return graph

time_step = 0
while True:
    part = 0
    visited = [[0] * k for _ in range(n)]
    for K in range(k):
        for N in range(n):
            if arr[N][K] != 0 and visited[N][K] == 0:
                part = part + 1
                visited = dfs(arr, K, N, visited, part)
    arr = melting(arr)
    if part >= 2:
        print(time_step)
        break
    s = 0
    for i in arr:
        s += sum(i)
    if s == 0:
        print(0)
        break
    time_step += 1