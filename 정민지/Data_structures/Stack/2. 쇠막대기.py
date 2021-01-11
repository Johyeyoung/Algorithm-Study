import sys

# 강의 풀이
#sys.stdin = open("input.txt", "rt")
s = input()
cnt = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':     # ( 이면 stack에 넣음
        stack.append(s[i])
    else:       # ) 이면 레이저인지 막대기인지 구분해야 함
        if s[i-1] == '(':   # 레이저인 경우 레이저 ( 꺼내고 막대기의 개수 더함
            stack.pop()
            cnt += len(stack)
        else:       # 막대기인 경우 막대기 ( 꺼내고 1더함
            stack.pop()
            cnt += 1

print(cnt)


