import sys

# ** 이전 납색 알고리즘 문제와 다른 점 : 한 유형당 한 개만 풀 수 있다는 조건!
# i) dp를 이차원 배열로 잡고 풀기 (단점: 메모리 많이 차지)
# ii) dp를 일차원 배열로 잡고, for문을 끝에서부터 돌기

# 강의 풀이
#sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
dp = [0] * (M + 1)  # dp[idx] : 제한 시간이 idx일 때 얻을 수 있는 최대 점수
                               # => 최종 답 : dp[M]

for i in range(N):
    s, t = map(int, input().split())
    for j in range(M, t-1, -1):
        dp[j] = max(dp[j], dp[j-t] + s) # dp[j] : 기존값
                # dp[j-t] + 1 : 새로 추가 (dp[j-t] : 현재 문제를 추가하기 전 얻을 수 있는 최대 점수)
print(dp[M])