import sys

#sys.stdin = open("input.txt", "rt")

N = int(input())
result = 0
lst = [[0 for _ in range(N+2)] for _ in range(N+2)]

for i in range(1, N+1):
    lst[i] = [0] + list(map(int, input().split())) + [0]

for i in range(1, N+1):
    for j in range(1, N+1):
        if (lst[i - 1][j] < lst[i][j]) and (lst[i + 1][j] < lst[i][j]) and \
                (lst[i][j - 1] < lst[i][j]) and (lst[i][j+1] < lst[i][j]):
            result += 1

print(result)
