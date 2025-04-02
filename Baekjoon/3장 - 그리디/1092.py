import sys

N = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

# 가장 무거운 박스를 들 수 있는 크레인이 없으면 종료
if crane[0] < box[0]:
    print(-1)
else:
    time = 0
    while box:
        c_index = 0  # 크레인 인덱스
        b_index = 0  # 박스 인덱스
        while c_index < N and b_index < len(box):
            if crane[c_index] >= box[b_index]:
                # 박스를 옮겼으니 제거하고 다음 크레인으로
                box.pop(b_index)
                c_index += 1
            else:
                # 이 박스는 현재 크레인이 못 드니까 다음 박스 확인
                b_index += 1
        time += 1  # 한 턴 종료
    print(time)