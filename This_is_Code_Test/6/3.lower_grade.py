## input
# 2
# 홍길동 95
# 이순신 77

import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())

arr = list()
for _ in range(n):
    arr.append(input().split(" "))

arr.sort(key=lambda x: x[1],reverse=False)

for a in arr:
    print(a[0], end =" ")