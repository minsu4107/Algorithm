import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
visited = [[0] * n for _ in range(n)]

def bfs(graph, start, visited):
    queue = deque([start])
    buildings = 0
    visited[start[1]][start[0]] = 1
    while queue:
        x, y = queue.popleft()
        buildings += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[ny][nx] != 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append([nx, ny])
    return buildings


result = []
for i in range(n):
    for j in range(n):
        if arr[j][i] != 0 and visited[j][i] ==0:
            result.append(bfs(arr, [i, j], visited))
            cnt += 1

print(cnt)
result.sort()
for i in result:
    print(i)