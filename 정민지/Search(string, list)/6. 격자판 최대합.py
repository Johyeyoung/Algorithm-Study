import sys

#sys.stdin = open("input.txt", "rt")

N = int(input())
result = 0
nums = []

for i in range(N):
    nums.append(list(map(int, input().split())))

# 행의 합
for i in range(N):
    guess = 0
    for j in range(N):
        guess += nums[i][j]

    result = max(result, guess)

# 열의 합
for i in range(N):
    guess = 0
    for j in range(N):
        guess += nums[j][i]

    result = max(result, guess)

# 두 대각선
guess = 0
for i in range(N):
    guess += nums[i][i]
result = max(result, guess)

guess = 0
for i in range(N):
    guess += nums[i][N-i-1]
result = max(result, guess)

print(result)
