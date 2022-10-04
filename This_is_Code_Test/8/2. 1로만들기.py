import os, sys

input = lambda : sys.stdin.readline().rstrip()


a = int(input())

n = [0] * 10000

for i in range(2, a + 1):
    n[i] = n[i-1] + 1

    if i % 5 == 0:
        n[i] = min(n[i], n[i // 2] +1)
    if i % 3 == 0:
        n[i] = min(n[i], n[i // 3] +1)
    if i % 5 == 0:
        n[i] = min(n[i], n[i // 5] + 1)

print(n[a])