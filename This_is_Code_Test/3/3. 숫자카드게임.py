# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4

import sys

input = lambda :sys.stdin.readline().rstrip()

m, k = map(int,input().split())

maxa = 0
for i in range(m):
    n_list = list(map(int, input().split()))
    # maxa = max(maxa, min(n_list))
    maxa = maxa if maxa > min(n_list) else min(n_list)
print(maxa)