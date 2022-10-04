import sys
sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(arr, x, y, visited, k):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if not visited[ny][nx] and arr[ny][nx] > k:
            visited[ny][nx] = True
            dfs(arr, nx, ny, visited, k)

result = 0
maxint = 0
for i in range(n):
    maxint = max(maxint, max(arr[i]))
for k in range(0, maxint):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[j][i] > k and not visited[j][i]:
                dfs(arr,i,j, visited, k)
                visited[j][i] = True
                cnt += 1
    result = max(result, cnt)

print(result)