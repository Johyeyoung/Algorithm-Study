import sys
from collections import deque

# 강의 풀이
#sys.stdin = open("input.txt", "rt")
N, K = map(int, input().split())
dq = deque(list(range(1, N+1)))

while dq:
    for _ in range(K-1):    # K-1번 queue에 앞에 있는 수 pop해서 append함
        dq.append(dq.popleft())
    dq.popleft()    # K번째 수 pop

    if len(dq) == 1:
        print(dq[0])
        dq.popleft()

