import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(N):
    min_A = min(A)
    max_B = max(B)
    result += min_A * max_B
    A.pop(A.index(min_A))
    B.pop(B.index(max_B))

print(result)