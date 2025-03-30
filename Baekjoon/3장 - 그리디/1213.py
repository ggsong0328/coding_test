import sys

name = sys.stdin.readline().rstrip()
N = len(name)

new_name = ''

count = {}

for n in name:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

odd = []

for value in count:
    if count[value] % 2:
        odd.append(value)

if len(odd) > 1:
    print("I'm Sorry Hansoo")
    
else:
    keys = count.keys()

    for key in sorted(keys): 
        new_name += key * (count[key] // 2)

    if odd:
        new_name = new_name + odd[0] + new_name[::-1]
    else:
        new_name = new_name + new_name[::-1]

    print(new_name)