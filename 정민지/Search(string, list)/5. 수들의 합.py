import sys

#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
cnt = 0
nums = list(map(int, input().split()))

for i in range(N):
    sum = nums[i]
    if sum == M:
        cnt += 1
        continue

    for j in range(i+1, N):
        sum += nums[j]
        if sum == M:
            cnt += 1
            break

        elif sum > M:
            break

print(cnt)


