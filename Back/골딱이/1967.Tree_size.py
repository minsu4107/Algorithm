import sys

input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10000)

n = int(input())
graph = [ [] for _ in range(n+1)]

for i in range(n-1):
    a, b, m = map(int, input().split())
    graph[a].append([b, m])
    graph[b].append([a, m])

distance = [-1] * (n+1)
distance[1] = 0

def dfs(start, distance, total_len):
    for node, length in graph[start]:
        if distance[node] == -1:
            distance[node] = length + total_len
            dfs(node, distance, length + total_len)


dfs(1, distance, 0)

max_idx = distance.index(max(distance))
distance = [-1] * (n+1)
distance[max_idx] = 0
dfs(max_idx, distance, 0)

print(max(distance))