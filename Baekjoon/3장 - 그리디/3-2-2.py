import sys

N, M, K = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))
data.sort()

first = data[N - 1]
second = data[N - 2]

count = int(M / (K + 1)) * K
count += M % (K + 1)

total = 0
total += (count) * first
total += (M - count) * second

print(total)