import sys

## input
# 5 8 3
# 2 4 5 4 6

n, m, k = map(int, input().split(" "))

num_list = list(map(int, input().split(" ")))
pop_count = 0
cnt = 0
sum = 0
while m > 0:
    max_num = max(num_list)
    idx = num_list.index(max_num)
    if pop_count < k:
        sum += max_num
        m -=1
        pop_count += 1
    else:
        num_list.pop(idx)
        sum += max(num_list)
        m -= 1
        pop_count = 0
        num_list.append(max_num)

print(sum)
