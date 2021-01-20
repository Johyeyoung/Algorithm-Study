# 쇠막대기(스택)

# 여는 괄호를 만나면 stack에 push!
# 닫는 괄호를 만나면 stack의 Top을 확인하고 Top이 여는 괄호이면 Top을 pop!
# 레이저가 있다는 것을 확인하면 쇠막대기 잘린 앞부분을 Count! - stack의 길이를 계산한다.
# 강의 코드
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':  # 여는 괄호를 만나는 경우
        stack.append(s[i])
    else:  # 닫는 괄호를 만나는 경우
        stack.pop()
        if s[i-1] == '(':  # 바로 앞이 여는 괄호이면 레이저로 판단!
            #stack.pop()
            cnt += len(stack)  # 레이저에 의해 잘린 쇠막대기 부분을 계산
        else:  # 바로 앞이 닫는 괄호이면 쇠막대기의 끝임을 판단!
            #stack.pop()
            cnt += 1  # 쇠막대기의 끝이므로 잘린 쇠막대기 1개를 추가!
print(cnt)