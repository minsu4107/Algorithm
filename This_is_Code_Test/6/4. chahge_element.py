## input

# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

import sys

input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())

arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

arr_1.sort()
arr_2.sort()

for i in range(1, k+1):
    max_ch = arr_2[-i]
    min_ch = arr_1[i-1]
    if max_ch > min_ch:
        arr_2[-i] = min_ch
        arr_1[i-1] = max_ch
    else:
        break

print(sum(arr_1))