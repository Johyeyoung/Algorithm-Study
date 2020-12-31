import sys

# sys.stdin = open("input.txt", "rt")
N = int(input())
coins = list(map(int, input().split()))
M = int(input())
dp = [float('inf')] * (M + 1)  # dp[idx] : 동전의 총 금액이 idx일 때 거슬러 줄 동전의 최소 개수
                               # => 최종 답 : dp[M]

for i in range(N):
    dp[coins[i]] = 1    # 최소 동전의 개수 구해야 함 => 만일 동전의 종류 == 동전의 총 금액 -> 1개만 필요
    for j in range(coins[i], M+1):
        dp[j] = min(dp[j], dp[j-coins[i]] + 1) # dp[j] : 기존값
                # dp[j-coins[i]] + 1 : 새로 추가 (dp[j-coins[i]] : 현재 동전을 추가하기 전 금액의 최소 동전의 개수)

print(dp[M])

