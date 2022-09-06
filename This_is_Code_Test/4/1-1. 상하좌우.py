## input
# 5
# R R R U D D

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
root = list(map(str, input().split()))

now_x, now_y = 1, 1
for direct in root:
    if direct == 'U' and now_x > 1:
        now_x -= 1
    elif direct == 'D' and now_x < n:
        now_x += 1
    elif direct == 'R' and now_x < n:
        now_y += 1
    elif direct == 'L' and now_x > 1:
        now_y -= 1

print(now_x, now_y)