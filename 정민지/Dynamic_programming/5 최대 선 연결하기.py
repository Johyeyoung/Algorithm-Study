import sys

# sys.stdin = open("input.txt", "rt")
N = int(input())
lst = list(map(int, input().split()))
dp = [0] * (N+1)

lst.insert(0, 0)
dp[1] = 1

# 왼쪽 -> 오른쪽 => 왼쪽의 숫자가 작을 수록 오른쪽의 idx값이 작아야 함
for i in range(2, N+1):
    max_val = 0
    for j in range(i-1, 0, -1):
        if (lst.index(j) < lst.index(i)) & (max_val < dp[j]):
            max_val = dp[j]
    dp[i] = max_val + 1

print(max(dp))

















