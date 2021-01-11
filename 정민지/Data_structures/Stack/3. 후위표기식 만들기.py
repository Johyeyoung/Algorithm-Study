import sys

# 강의 풀이
# sys.stdin = open("input.txt", "rt")
s = input()
result = ""
stack = []  # 연산자 들어감

# stack에 연산자 들어가는 경우
# 1. + or - 인 경우 : *나 / 계산해줘야 함
# 2. * or / 인 경우 : stack에 *나 /가 들어있는 경우 먼저 들어간 연산자 계산해줘야 함
# 3. ( 인 경우 : 그냥 들어감
# 4. ) 인 경우 : stack에서 ( 가 나오기 전 연산자 모두 계산해줘야 함

for i in s:
    if i.isdecimal():
        result += i
    else:   # 연산자
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and (stack[-1] != '('):     # stack안에 * ( + - 인 경우 *보다 +, -의 우선순위가 더 높다
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and (stack[-1] != '('):
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)
