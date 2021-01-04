import sys

# isdecimal() : 0~9까지의 숫자 형태의 스트링 참
# isdigit() : 모든 형태의  숫자 형태의 스트링 참  

def find_divisor(n):
    divisor = set()
    for i in range(1, n//2):
        if n % i == 0:
            divisor.add(i)
            divisor.add(n/i)
    #print(divisor)
    return len(divisor)

# sys.stdin = open("input.txt", "rt")
s = input()
result = ""
for i in s:
    if i.isdigit():
        result += i

print(int(result))
print(find_divisor(int(result)))

# 강의 풀이
# 나의 풀이 : 스트링에 숫자(string형) 더해서 int형으로 바꿈 
# res = 0
# res = res * 10 + int(x)