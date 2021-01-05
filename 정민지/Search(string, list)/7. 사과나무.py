import sys

#sys.stdin = open("input.txt", "rt")

N = int(input())
result = 0
start, end = N//2, N//2
nums = []

for i in range(N):
    nums.append(list(map(int, input().split())))

for i in range(N):
    for j in range(start, end+1):
        #print(nums[i][j])
        result += nums[i][j]
    if i < N//2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1
    #print("Start: ", start, " end: ", end)

print(result)
