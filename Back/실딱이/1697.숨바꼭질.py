import sys

from collections import deque

input = lambda : sys.stdin.readline().rstrip()
visited = [0] * (100000 * 2 +1)

N, K = map(int, input().split())

def bfs(start, target,visited):
    queue = deque([start])
    visited[start] = 1
    while visited[target] == 0:
        i = queue.popleft()
        # print(i)
        if i == target:
            return visited[target]
        for n in [2 * i, i-1, i + 1]:
            if n > 100000 or n < 0:
                continue
            if not visited[n]:
                queue.append(n)
                visited[n] = visited[i] + 1
    return visited[target]

print(bfs(N, K, visited) -1)