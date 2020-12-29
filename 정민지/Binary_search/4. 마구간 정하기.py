import sys

# 강의 풀이
def Count(len):     # len : 최대 거리가 될 수 있는 예비 답
    cnt = 1
    ep = lst[0] # 마구간의 첫번째 자리부터 endpoint시작
    for i in range(1, N):
        if lst[i] - ep >= len:  # 최대 거리를 넘는다면 카운트 올림
            cnt += 1
            ep = lst[i]     # endpoint갱신
    return cnt

# sys.stdin = open("input.txt", "rt")
N, C = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))


lst.sort()
lower = lst[0]
upper = lst[-1]
result = 0

while lower <= upper:
    mid = (lower + upper) // 2
    if C <= Count(mid): # 답이 될 수 있음
        result = mid
        lower = mid + 1     # 최대 거리를 구해야하기 때문에 최소값 올림
    else:
        upper = mid - 1


print(result)



























