import sys

input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
INF = float('inf')
graph = [[INF] * n for _ in range(n) ]
for i in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for i in range(n):
    graph[i][i] = 0

end, meet = map(int, input().split())

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if graph[0][meet-1] != float('inf') and graph[meet-1][end-1] != float('inf'):
    print(graph[0][meet-1] + graph[meet-1][end-1])
else:
    print("-1")


##input
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
