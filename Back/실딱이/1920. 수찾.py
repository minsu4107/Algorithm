import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
target_list = list(map(int, input().split()))

k = int(input())
req_list = list(map(int, input().split()))


def binary(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        # print(f"start = {start} \t end = {end} \t mid = {mid}")
        if arr[mid] == target:
            return "1"
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "0"

target_list.sort()
# print(target_list)
for part in req_list:
    print(binary(target_list, 0, n-1, part))
