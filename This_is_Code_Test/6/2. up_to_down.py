##input
# 3
# 15
# 27
# 12
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

abcd = []
for _ in range(n):
    abcd.append(int(input()))

abcd.sort(reverse=True)
print(*abcd)