# 1. 회문 문자열 검사

s ="level"

s=s.upper()

size = len(s)

for i in range(size//2):
    if s[i] != s[-1-i]:
        print("NO")
        break
    else:
        print("YES")
        break


#s==s[::-1] 