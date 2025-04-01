import sys

N = int(sys.stdin.readline())
d_num = list(map(int, sys.stdin.readline().split()))

# 마주보는 면 인덱스
opposite = [5, 4, 3, 2, 1, 0]

# 최소 한 면
min1 = min(d_num)

# 두 면의 최소 합 (마주보는 면 제외)
min2 = float('inf')
for i in range(6):
    for j in range(i + 1, 6):
        if j != opposite[i]:
            min2 = min(min2, d_num[i] + d_num[j])

# 세 면의 최소 합 (꼭짓점 조합)
corner_cases = [
    (0, 1, 2), (0, 2, 4), (0, 3, 1), (0, 3, 4),
    (5, 1, 2), (5, 2, 4), (5, 3, 1), (5, 3, 4)
]
min3 = float('inf')
for a, b, c in corner_cases:
    min3 = min(min3, d_num[a] + d_num[b] + d_num[c])

# N = 1은 예외 처리
if N == 1:
    print(sum(d_num) - max(d_num))
    sys.exit()

# N >= 2일 때 겉면 처리
# 3면 보이는 꼭짓점: 4개 (윗면) + 4개 (아랫면) = 8개
count_3 = 4

# 2면 보이는 모서리: 4 * (N - 2) + 4 * (N - 1) = 8N - 12
count_2 = 4 * (N - 2) + 4 * (N - 1)

# 1면 보이는 면 중앙: (N - 2)^2 + (N - 2)*(N - 1)*4
count_1 = (N - 2) * (N - 2) + (N - 2) * (N - 1) * 4

# 최종 계산
result = 0
result += min3 * 4        # 꼭짓점
result += min2 * count_2  # 모서리
result += min1 * count_1  # 한 면만 보이는 면

print(result)