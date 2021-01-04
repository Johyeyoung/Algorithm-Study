import sys

def palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

#sys.stdin = open("input.txt", "rt")
N = int(input())

for i in range(N):
    s = input()
    s = s.lower()
    if palindrome(s):
        print(f"#{i+1} YES")
    else:
        print(f"#{i + 1} NO")

# 강의 풀이 (palindrome 더 간단하게)
# if s == s[::-1] => True (원래 문자열 == 뒤집은 문자열)