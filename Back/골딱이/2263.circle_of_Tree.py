import sys

sys.setrecursionlimit(100000)

input = lambda : sys.stdin.readline().rstrip()

n = int(input())

in_ = list(map(int, input().split()))
post_ = list(map(int, input().split()))

position = [0] * (n+1)
for i in range(n):
    position[in_[i]] = i
def pre_order(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    root = post_[post_end]
    print(root, end = ' ')

    left_ = position[root] - in_start
    right_ = in_end - position[root]

    pre_order(in_start, in_start+left_ -1, post_start, post_start + left_ -1)
    pre_order(in_end-right_+1, in_end, post_end-right_, post_end -1)

pre_order(0, n-1, 0, n-1)