import sys

exp = sys.stdin.readline().strip()

parts = exp.split('-')

initial = sum(map(int, parts[0].split('+')))

rest = 0
for part in parts[1:]:
    rest += sum(map(int, part.split('+')))

print(initial - rest)