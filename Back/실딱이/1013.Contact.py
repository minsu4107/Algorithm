import sys
import re

input = lambda : sys.stdin.readline().rstrip()

n = int(input())

answer = []

for _ in range(n):
    re_str = input()

    p = re.compile(r'(100+1+|01)+')
    m = p.fullmatch(re_str)
    if m: answer.append('YES')
    else: answer.append('NO')

for _ in answer:
    print(_)