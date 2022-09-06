##input
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

n, m = map(int,input().split())

graph = []
dx = [-1, 0 ,1 ,0]
dy = [0, -1, 0 ,1]

for _ in range(n):
    graph.append(list(map(int,input())))

print(graph)
def bfs(graph, start):
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx <0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 1:
                queue.append([nx,ny])
                graph[ny][nx] = graph[y][x]+1
    return graph[n-1][m-1]

print(bfs(graph, [0,0]))