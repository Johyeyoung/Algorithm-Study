import sys

# 강의 풀이
# sys.stdin = open("input.txt", "rt")
N = int(input())
lst = []
dp = [0] * (N+1)    #dp[idx] = idx번째 벽돌이 가장 위에 있을 때 탑의 최대 높이

for i in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x:x[0], reverse=True)   # 넓이 기준으로 내림차순 정렬 => 넓이 고려 x , 무게만 고려하면 됨
dp[0] = lst[0][1]

for i in range(1, N):
    max_top = 0
    for j in range(i-1, -1, -1):
        if (lst[i][2] < lst[j][2]) & (max_top < dp[j]):
            max_top = dp[j]
    dp[i] = max_top + lst[i][1]

print(max(dp))
























