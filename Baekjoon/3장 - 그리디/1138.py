import sys

N = int(sys.stdin.readline())

left_count = list(map(int, sys.stdin.readline().split()))

order = [None] * N

for i in range(N):
    height = i + 1
    left = left_count[i]
    count = 0
    for j in range(N):
        if order[j] is None:
            if count == left:
                order[j] = height
                break
            count += 1

print(*order)