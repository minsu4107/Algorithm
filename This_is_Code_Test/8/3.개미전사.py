import sys

input = lambda : sys.stdin.readline().rstrip()

## input

# 4
# 1 3 1 5

n = int(input())
arr = list(map(int, input().split()))

dp_list = [0] * 1000
dp_list[0] = arr[0]
dp_list[1] = arr[1]

for i in range(2 , n):
    dp_list[i] = max(dp_list[i-1], dp_list[i-2] + arr[i])

print(max(dp_list[:n+1]))