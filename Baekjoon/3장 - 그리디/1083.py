import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())

for i in range(N):
    if S <= 0:
        break

    max_idx = i
    for j in range(i + 1, min(N, i + S + 1)):
        if A[j] > A[max_idx]:
            max_idx = j

    moves = max_idx - i

    if moves <= S:
        max_value = A[max_idx]
        for j in range(max_idx, i, -1):
            A[j] = A[j - 1]
        A[i] = max_value
        S -= moves

print(*A)