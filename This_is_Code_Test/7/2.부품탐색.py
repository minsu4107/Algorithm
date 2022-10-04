import sys, time


## input
# 5
# 8 3 7 9 2
# 3
# 5 7 9
## 일반 구현
# input = lambda : sys.stdin.readline().rstrip()
#
# own = int(input())
#
# own_list = list(map(int, input().split()))
#
# req = int(input())
# req_list = list(map(int, input().split()))
#
# flag = True
#
# for part in req_list:
#     try:
#         if own_list.index(part) != -1:
#             print('yes')
#     except ValueError:
#         print('no')

input = lambda : sys.stdin.readline().rstrip()

own = int(input())

own_list = list(map(int, input().split()))

req = int(input())
req_list = list(map(int, input().split()))


def binary(tree, start, end,target):
    while start < end:
        mid = (start + end) // 2
        if tree[mid] == target:
            return 'yes'
        elif tree[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 'no'

own_list.sort()

for part in req_list:
    print(binary(own_list, 0, own,part))




