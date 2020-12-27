import sys

# 인강 풀이(Bottom-Up)
# sys.stdin = open("input.txt", "rt")
N = int(input())
lst = []
dp = [[0] * N for _ in range(N)]

for i in range(N):
    lst.append(list(map(int, input().split())))

dp[0][0] = lst[0][0]

for i in range(N):
    dp[0][i] = dp[0][i-1] + lst[0][i]
    dp[i][0] = dp[i-1][0] + lst[i][0]

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + lst[i][j]

print(dp[N-1][N-1])

# 인강 풀이(Top_Down)
# def dfs(x, y):
#     if dp[x][y] > 0:
#         return dp[x][y]
#
#     if x == 0 and y == 0:
#         return lst[0][0]
#     else:
#         if y == 0:
#             dp[x][y] = dfs(x-1, y) + lst[x][y]
#         elif x == 0:
#             dp[x][y] = dfs(x, y-1) + lst[x][y]
#         else:
#             dp[x][y] = min(dfs(x, y-1), dfs(x-1, y)) + lst[x][y]
#         return dp[x][y]

























