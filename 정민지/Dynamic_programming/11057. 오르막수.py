import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
mod = 10007
dp = [1] * 10    # 마지막 자리 숫자가 인덱스(1~9)일 때 오르막수 저장 

for _ in range(n-1):
    for j in range(1, 10):
        dp[j] = (dp[j-1] + dp[j]) % mod   # 새로운 오르막수(현재 마지막 자릿수-1에 저장되어 있는 오르막수) + 현재 저장되어 있는 오르막수

print(sum(dp) % mod)
