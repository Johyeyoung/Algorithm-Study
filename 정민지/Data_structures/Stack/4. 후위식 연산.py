import sys

#sys.stdin = open("input.txt", "rt")
s = input()
result = ""
stack = []  # 숫자 들어감

for i in s:
    if i.isdecimal():
        stack.append(int(i))

    else:
        right_val = stack.pop()
        left_val = stack.pop()
        if i == '+':
            stack.append(left_val + right_val)
        elif i == '-':
            stack.append(left_val - right_val)
        elif i == '*':
            stack.append(left_val * right_val)
        elif i == '/':
            stack.append(left_val / right_val)

print(stack[0])
