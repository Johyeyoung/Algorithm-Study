import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")
s = input()
N = int(input())
dq = []

for i in range(N):
    check = s
    dq = [i for i in input()]
    dq = deque(dq)

    while dq:
        cur = dq.popleft()  # queue의 제일 앞 원소
        if cur in check:    # 필수 과목의 과목이라면
            if cur == check[0]:     # 필수 과목의 제일 첫 번째 과목이라면 check에서 과목 지움
                check = check[1:]
            else:
                print(f"#{i+1} NO")     # 필수 과목의 첫 번째 과목이 아니라면 바로 break
                break
        if len(check) == 0: # check의 길이가 0이라면 순서대로 과목 설계한 것이므로 YES
            print(f"#{i+1} YES")
            break
    else:   # 필수 과목이 수업 설계에 없는 경우 -> queue를 다 돌았음에도 불구하고 필수 과목이 남아 있다
        if len(check) > 0:
            print(f"#{i+1} NO")
        # print("check: ", check)
        # print("cur: ", cur)