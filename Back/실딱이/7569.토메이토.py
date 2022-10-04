import sys
from collections import deque


input = lambda : sys.stdin.readline().rstrip()

n, m, h = map(int, input().split())

arr = [[] for _ in range(h)]

for i in range(h):
    for j in range(m):
        arr[i].append(list(map(int,input().split())))

tomato = []
for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k] == 1:
                tomato.append([i,j,k])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque(tomato)
    cnt = -1
    while queue:
        qlen = len(queue)
        cnt +=1
        while qlen:
            z, y, x = queue.popleft()
            for i in range(6):
                nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
                if nz <= -1 or nz >= h or ny <= -1 or ny >= m or nx <= -1 or nx >= n:
                    continue
                if arr[nz][ny][nx] == 0:
                    arr[nz][ny][nx] = 1
                    queue.append([nz, ny, nx])
            qlen -=1
    return cnt

def zero_found(arr):
    flag = True
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if arr[i][j][k] ==0:
                    flag = False
                    return flag
    return flag

result = bfs()
print(result if zero_found(arr) else -1 )
