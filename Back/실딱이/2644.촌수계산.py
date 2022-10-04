import sys
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

start, end = map(int, input().split())

k = int(input())

graph = defaultdict(list)

for i in range(k):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0] * (n+1)
def bfs(graph, start, dest, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        i = queue.popleft()
        if i == dest:
            return visited[i]
        for node in graph[i]:
            if not visited[node]:
                visited[node] = visited[i] + 1
                queue.append(node)
    return -1

answer = bfs(graph, start, end, visited)
print(answer -1 if answer != -1 else answer )
