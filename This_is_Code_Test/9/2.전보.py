import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

n, m, dest = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [float('inf')] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[0] = 0
    while q:
        value, node = heapq.heappop()

        if distance[node] < value:
            continue

        for n in graph[node]:
            cost = value + n[1]
            if cost < distance[n[0]]:
                distance[n[0]] = cost
                heapq.heappush(q, (cost, n[0]))
