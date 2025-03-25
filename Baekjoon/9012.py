import sys

T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    br = sys.stdin.readline().strip()
    for b in br:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")