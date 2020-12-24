import sys
from collections import deque

# sys.stdin = open("input.txt", "rt")
K = int(input())
q = deque(list(map(int, input().split())))
result = ''
pre = 0


# 1. [0]과 [-1] 비교 => 작은 값
# 2. 2의 작은 값이 수열의 마지막보다 큰 지 확인
# 2-1 작다면 다른 끝 값과 비교해서 다른 끝 값 충족하면 추가, 아니면 break
# 2-2 크다면 수열에 추가
while q:
    if (q[0] < pre) & (q[-1] < pre):
        break

    if len(q) == 1:
        result += 'L'
        break

    if q[0] < q[-1]:
        if pre < q[0]:
            result += 'L'
            pre = q[0]
            q.popleft()
        else:
            if pre < q[-1]:
                result += 'R'
                pre = q[-1]
                q.pop()
            else:
                break

    else:
        if pre < q[-1]:
            result += 'R'
            pre = q[-1]
            q.pop()
        else:
            if pre < q[0]:
                result += 'L'
                pre = q[0]
                q.popleft()
            else:
                break
    # print("pre: ", pre)

print(len(result))
print(result)








