import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")
N, K = map(int, input().split())
dq = [[i, j] for i, j in enumerate(list(map(int, input().split())))]    # 몇 번째 환자인지 구분하기 위해 [순서, 위험도]
dq = deque(dq)                                                          # 형식으로 deque에 저장
result = 0

while dq:
    cur = dq[0][1]  # 제일 앞에 있는 환자의 위험도
    for i in range(1, len(dq)):
        if cur < dq[i][1]:  # cur이 뒤에 있는 환자의 위험도 보다 작다면 꺼내서 제일 뒤에 추가
            dq.append(dq.popleft())
            break
    else:   # cur이 제일 높다면 꺼내고 진료 카운트 1증가
        if dq[0][0] == K:   # 만일 K번째 환자일 경우 값 출력하고 break
            print(result + 1)
            break
        dq.popleft()
        result += 1
    #print(dq)


# 강의 풀이
# cur = dq.popleft()
# if any(cur[1] < x[1] for x in dq)