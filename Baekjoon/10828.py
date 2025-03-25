import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    command = sys.stdin.readline()
    
    if 'push' in command:
        stack.append(int(command[5:]))
        #print(stack)
    elif 'pop' in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])