import sys

# sys.stdin = open("input.txt", "rt")

# 강의 풀이 
N = int(input())
lst = list(map(int, input().split()))
dp = [0] * (N+1)

lst.insert(0, 0)
dp[1] = 1   # dp[idx] = lst[idx]가 마지막 항이라고 생각 -> 수열의 최대 길이

for i in range(2, N+1):
    max_len = 0
    for j in range(i-1, 0, -1):     # lst에서 i 앞에 있는 수 중 lst[i] 보다 작고, dp값이 제일 큰 값 찾는다.
        if lst[j] < lst[i] and dp[j] > max_len:
            max_len = dp[j]
    dp[i] = max_len + 1


print(max(dp))
















