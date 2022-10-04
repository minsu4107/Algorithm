import sys

input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

value_list = [ int(input()) for i in range(n) ]

can_change = [10001] * (m+1)

can_change[0] = 0

for i in range(1, m+1):
    for coin in value_list:
        if i - coin >= 0 and can_change[i-coin] < 10001:
            can_change[i] = min(can_change[i], can_change[i-coin]+1)


print(can_change[m] if can_change[m] != 10001 else -1)