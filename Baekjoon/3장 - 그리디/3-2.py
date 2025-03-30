import sys

N, M, K = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))
data.sort()

first = data[N - 1]
second = data[N - 2]

total = 0

while True:
    for i in range(K):
        if M == 0:
            break
        total += first
        M -= 1
    if M == 0:
        break
    total += second
    M -= 1

print(total)