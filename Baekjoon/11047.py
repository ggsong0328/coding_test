import sys

N, K = map(int, sys.stdin.readline().split())

A = []
for _ in range(N):
    money = int(sys.stdin.readline())
    A.append(money)

A.sort(reverse=True)
count = 0

for coin in A:
    if coin <= K:
        count += K // coin 
        K %= coin          

print(count)