import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())

dp = [0] * (N+1)    # 인덱스와 숫자 맞추기 위해 0번째 값 0으로 초기화
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])

# 강의 풀이(Top-Down : 재귀, 메모이제이션)

# def DFS(len):
#     if dy[len] > 0:
#         return dy[len]
#
#     if len == 1 or len == 2:
#         return len
#     else:
#         dy[len] = DFS(len-1) + DFS(len-2)
#         return dy[len]
#
#
# if __name__ == '__main__':
#     n = int(input())
#     dy = [0] * len(n+1)
#     print(DFS(n))










