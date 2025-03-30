import sys

N, M = map(int, sys.stdin.readline().split())

six = []
one = []

for _ in range(M):
    s, o = map(int, sys.stdin.readline().split())
    six.append(s)
    one.append(o)

min_six = min(six)
min_one = min(one)

ans = 0

while True:
    if N <= 0:
        break
    
    elif N <= 6:
        min_val = min(min_six, min_one * N)
        ans += min_val
    elif N > 6:
        min_val = min(min_six, min_one * 6)
        ans += min_val
    
    N -= 6

print(ans)