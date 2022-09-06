import sys

input = lambda : sys.stdin.readline().rstrip()

n, m = list(map(int, input().split()))

mold = list()
for _ in range(n):
    mold.append(list(map(int, input().split())))

def dfs(x, y):
    if -1 <= x <= m or -1  -1 <= y <= n:
        return False

    if mold[x][y] == 0:
        mold[x][y] = 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

cnt =0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt +=1

print(cnt)