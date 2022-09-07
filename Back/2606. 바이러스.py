import sys
from collections import Counter

input = lambda : sys.stdin.readline().rstrip()

n = int(input())

m = int(input())

graph = [ [] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
def dfs(graph, start, visited):
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

dfs(graph, 1, visited)

print(Counter(visited)[True] -1)