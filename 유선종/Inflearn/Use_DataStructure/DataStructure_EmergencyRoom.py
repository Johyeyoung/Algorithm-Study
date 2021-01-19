# 응급실

# 내가 작성한 코드
from collections import deque

n, m = map(int, input().split())
danger = list(map(int, input().split()))
danger = deque(danger)
dgIndex = list(range(n))
dgIndex = deque(dgIndex)
mPatient = danger[m]
cnt = 0
while m in dgIndex:
    dg = danger[0]
    if dg < max(danger):
        tmp = danger.popleft()
        danger.append(tmp)
        tmp1 = dgIndex.popleft()
        dgIndex.append(tmp1)
    else:
        danger.popleft()
        dgIndex.popleft()
        cnt += 1
print(cnt)

# 강의 코드
