#  공주 구하기(큐)

# deque 이용 - append, popleft
# 내가 작성한 코드
from collections import deque

n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
cnt = 1
while len(dq) > 1:
    if cnt == k:
        dq.popleft()
        cnt = 1
    else:
        a = dq.popleft()
        dq.append(a)
        cnt += 1
print(dq[0])

# 강의 코드