import sys

##input
# a1

input = sys.stdin.readline().rstrip()

ab = str(input)

a, b = ab[0], ab[1]

# x_axis = [chr(i) for i in range(ord('a'),ord('h')+1)]
x_axis ='abcdefgh'
x = x_axis.index(a) + 1

y = int(b)
cnt = 0
x_add = [-2, -1, 1, 2]
y_add = [-2, -1, 1, 2]
for i in x_add:
    for j in y_add:
        if abs(i) + abs(j) == 3 and 0 < x + i <= 8 and 0 < y + j <= 8:
            cnt += 1

print(cnt)

