print('+와 -를 번걸아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for _ in range(n // 2):
    print('+-', end ='')

if n % 2:
    print('+', end='') # n이 홀수일 때만 +를 출력

print()