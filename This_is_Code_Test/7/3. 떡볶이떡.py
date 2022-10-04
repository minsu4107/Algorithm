import sys

input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

dduk_list = list(map(int, input().split()))

dduk_list.sort()


def binary(tree, start, end, target):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for dduk in tree:
            if dduk > mid:
                total += dduk - mid
        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
        # print(f"start = {start} \t end = {end} \t mid = {mid} \t result = {result}")
    return result

print(binary(dduk_list, 0, max(dduk_list), m))