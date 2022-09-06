import sys


## input
# 5 8 3
# 2 4 5 4 6


sys.stdin = open("2_input.txt", "r")

n,m,k = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

max_num = num_list[n - 1]
sec_num = num_list[n - 2]

count = (m // (k+1)) * k + m % (k+1)

sum = 0
sum += count * max_num
sum += (m - count) * sec_num

print(sum)


