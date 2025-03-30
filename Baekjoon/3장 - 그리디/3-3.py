import sys

N, M = map(int, sys.stdin.readline().split())

result = 0

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    min_data = min(data)
    if result < min_data:
        result = min_data

print(result)