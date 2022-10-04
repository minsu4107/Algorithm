import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

f, start, go, up, down = map(int, input().split())

visited = [0] * (f+1)



def bfs(start, target, visited):
    queue = deque([start])
    visited[start] = 1

    while visited[target] == 0:
        i = queue.popleft()
        for node in [i + up, i-down]:
            if node > f or node <= 0:
                continue
            if not visited[node]:
                queue.append(node)
                visited[node] = visited[i] + 1
        if len(queue) == 0:
            return "use the stairs"
    return visited[target] - 1

print(bfs(start, go, visited))