import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()


n, m = map(int, input().split())

arr = [ list(map(int, input().split())) for _ in range(m)]

tomato = []
for i in range(n):
    for j in range(m):
        if arr[j][i] == 1:
            tomato.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    que = deque(tomato)
    count = -1
    while que:
        qlen = len(que)
        while qlen:
            x,y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue
                if arr[ny][nx] == 0:
                    arr[ny][nx] = 1
                    que.append([nx, ny])
            qlen -= 1
        count += 1
    return count


def zero_found(arr):
    flag = True
    for j in range(m):
        for k in range(n):
            if arr[j][k] == 0:
                flag = False
                return flag
    return flag
result = bfs()
print(result if zero_found(arr) else -1)