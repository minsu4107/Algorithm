import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())

arr = [ list(map(int, input().split())) for _ in range(n)]

arr_0 = sorted(arr, key=lambda x: x[0])
arr_1 = sorted(arr_0, key=lambda x: x[1], reverse = True)

min_x = arr_1[0][0]
max_x = arr_1[0][0]
max_high = arr_1[0][1]

result = arr_1[0][1]
for x, high in arr_1:
    if x < min_x:
        result += abs(x - min_x) * high
        min_x = x
    elif x > max_x:
        result += abs(max_x - x) * high
        max_x = x
print(result)