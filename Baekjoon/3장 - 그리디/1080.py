import sys

N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

count = 0

for i in range(N - 2): 
    for j in range(M - 2):
        if A[i][j] != B[i][j]:  
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    A[k][l] = 1 - A[k][l]  
            count += 1

if A == B:
    print(count)
else:
    print(-1)