import sys


##input
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

input = lambda : sys.stdin.readline().rstrip()

w, h = list(map(int, input().split()))

x, y, d = list(map(int, input().split()))

map_ = list()
for i in range(w):
    map_.append(list(map(int, input().split())))
visited = [[0] * w for _ in range(h)]
##### 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0
visited[y][x] = 1
d_cnt = 0
while True:
    d = (d - 1) % 4
    ny = y + dy[d]
    nx = x + dx[x]

    if visited[ny][nx] == 0 and map_[ny][nx] == 0:
        visited[ny][nx] = 1
        x, y = nx, ny
        cnt += 1
        d_cnt = 0
        continue
    else:
        d_cnt +=1
    if d_cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if map_[ny][nx] == 0:
            x = nx
            y = ny
        else:
            break
        d_cnt =0
print(cnt)