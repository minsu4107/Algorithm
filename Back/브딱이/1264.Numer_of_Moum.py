import sys
import re

input = lambda : sys.stdin.readline().rstrip()

while True:
    summ= 0
    string_ = input()
    if string_ == '#':
        break
    for re_str in ['a','e', 'i', 'o', 'u', 'A','E','I','O','U']:
        p = re.compile(re_str)
        re_result = p.findall(string_)
        summ += len(re_result)
    print(summ)
