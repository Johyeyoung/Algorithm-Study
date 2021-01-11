import sys

# 강의 풀이
# sys.stdin = open("input.txt", "rt")
num, m = map(int, input().split())
stack = []
num = [int(i) for i in str(num)]
# == num = list(map(int, str(num)))

for i in num:
    while stack and m > 0 and stack[-1] < i:
        stack.pop()
        m -= 1
    stack.append(i)

if m > 0:
    stack = stack[:-m]

for i in stack:
    print(i, end='')

# == ''.join(map(str, stack))