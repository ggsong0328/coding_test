import sys

N = int(sys.stdin.readline())

change = [500, 100, 50, 10]

count = 0

for coin in change:
    if coin <= N:
        count += N // coin
        N %= coin

print(count)