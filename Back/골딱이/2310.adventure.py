import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

def bfs(graph,maze, gold, start,end, visited):
    q = deque([[start,0]])

    while q:
        node, have = q.popleft()
        if node == end:
            return True
        for n in graph[node]:
            if maze[n] == 'E':
                if visited[n][have] == True:
                    continue
                visited[n][have] = True
                q.append([n, have])
            elif maze[n] == 'L':
                have = gold[n] if have < gold[n] else have
                if visited[n][have] == True:
                    continue
                visited[n][have] = True
                q.append([n, have])
            elif maze[n] == 'T':
                if have < gold[n]:
                    continue
                have -= gold[n]
                if visited[n][have] == True:
                    continue
                visited[n][have] = True
                q.append([n, have])
    return False

while True:
    n = int(input())
    if n == 0:
        break
    maze = [[] for _ in range(n+1)]
    gold = [[] for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        tmp = input().split()
        maze[i] = tmp[0]
        gold[i] = int(tmp[1])
        for j in range(2, len(tmp)-1):
            graph[i].append(int(tmp[j]))

    visited = [[False] * 501 for _ in range(n + 1)]
    if bfs(graph, maze, gold, 1,n, visited):
        print("Yes")
    else:
        print("No")

