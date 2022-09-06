## input

# 10 13
# 1 3 5 7 9 11 13 15 17 19

import sys

input = lambda: sys.stdin.readline().rstrip()


def bi_search(arr, target, start, end):
    if start > end:
        print(start, end)
        return None
    mid = (start + end) // 2
    print(start, mid, end, arr[start:end+1])
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        result = bi_search(arr, target, start, mid - 1)
    else:
        result = bi_search(arr, target, mid+1, end)
    return result

n, target = map(int, input().split())

arr = list(map(int, input().split()))
print(bi_search(arr, target, 0, n-1))


arr = [ [] for _ in range(10)]