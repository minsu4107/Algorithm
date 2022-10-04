import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr_stair = [ int(input()) for _ in range(n) ]

best_arr = [ [0,0] for i in range(n+1)]

arr_stair.insert(0, 0)

best_arr[1][0] = 1
best_arr[1][1] = arr_stair[1]

for i in range(2, n+1):
    if best_arr[i-1][0] >= 2:
        best_arr[i][0] = 1
        best_arr[i][1] = max(best_arr[i-1][1] - arr_stair[i-1]+ arr_stair[i], best_arr[i-2][1] + arr_stair[i])
    else:
        best_arr[i][0] = best_arr[i - 1][0] + 1
        best_arr[i][1] = max(best_arr[i-1][1] +arr_stair[i], best_arr[i-2][1] +arr_stair[i])
    print(best_arr)

print(best_arr[n][1])