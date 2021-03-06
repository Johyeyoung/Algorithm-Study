import sys

#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
coins = []
dp = [0] * (k + 1)    # dp[i] : 가치의 합이 i원인 경우의 수

for i in range(n):
    coins.append(int(input()))

dp[0] = 1

for i in coins: # -@
    for j in range(1, k+1):
        if 0 <= j - i:
            dp[j] += dp[j - i]  # dp[j]는 결국 주어진 coin의 값을 뺀 금액에서 coin을 더해야 한다. 따라서 dp[j-coins]의 값을 더해주면 된다. -@@
            
# @@의 예)
# coins[0] = 2라고 가정 => 그렇다면 가치의 합이 5원인 경우의 수는 5-2 = 3, 가치의 합이 3이 되는 경우를 더해주면 됨
# => dp[5] = dp[5-2] + dp[5]
# => 주어진 동전을 리스트 넣어 한 번씩 검사함 - @
            

print(dp[k])
