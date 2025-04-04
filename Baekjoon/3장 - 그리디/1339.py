import sys

N = int(sys.stdin.readline())
words = []
for i in range(N):
    word = list(map(str, sys.stdin.readline().rstrip()))
    words.append(word)

weight = {}

for i in range(len(words)):
    for j in range(len(words[i])):
        ch = words[i][j]
        weight[ch] = weight.get(ch, 0) + 10**(len(words[i]) - j - 1)

#print(weight)

num = 9
sorted_weight = sorted(weight.items(), key=lambda item:item[1], reverse=True)

for k, v in sorted_weight:
    weight[k] = num
    num -= 1

#print(weight)

result = 0

for i in range(len(words)):
    for j in range(len(words[i])):
        words[i][j] = weight.get(words[i][j]) * (10**(len(words[i]) - j -1))
        result += words[i][j]


        
print(result)