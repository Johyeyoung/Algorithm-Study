import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
mod = 15746
dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[n] % mod)
