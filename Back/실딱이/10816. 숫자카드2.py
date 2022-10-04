import sys
from bisect import bisect_left, bisect_right

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
target_list = list(map(int, input().split()))

k = int(input())
req_list = list(map(int, input().split()))
# 시간초과 코드
# def binary(arr, start, end, target):
#     while start <= end:
#         mid = (start + end) // 2
#         # print(f"start = {start} \t end = {end} \t mid = {mid}")
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             start = mid +1
#         else:
#             end = mid - 1
#     return -1
#
# target_list.sort()
# # print(target_list)
# result = []
# for part in req_list:
#     # print(f"part = {part}")
#     cnt = 0
#     one_ = binary(target_list, 0, n-1, part)
#     if one_ != -1:
#         cnt = 1
#         tmp = one_ + 1
#         while tmp <= n-1:
#             if target_list[tmp] == target_list[tmp - 1]:
#                 tmp += 1
#                 cnt += 1
#             else:
#                 break
#         tmp = one_
#         while tmp >= 1:
#             if target_list[tmp] == target_list[tmp - 1]:
#                 tmp -= 1
#                 cnt += 1
#             else:
#                 break
#     result.append(cnt)

target_list.sort()
for part in req_list:
    left = bisect_left(target_list, part)
    right = bisect_right(target_list,part)
    print(right-left, end = ' ')