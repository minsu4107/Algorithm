import sys

input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())

summ = 0
while n >= k:
    n /= k
    summ +=1
if n % k != 1:
    summ += n % k -1

print(summ)