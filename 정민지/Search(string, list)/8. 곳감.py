import sys

#sys.stdin = open("input.txt", "rt")

N = int(input())
result = 0
start, end = N//2, N//2
nums = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
lst = [list(map(int, input().split())) for _ in range(M)]

# 위치 옮기기
# 풀이 i) 문제점 : num(회전하는 격자 수)이 리스트 개수보다 클 때 결과가 다르게 나옴
# for i in lst:
#     row, dir, num = i
#     if dir == 0:
#         nums[row - 1] = nums[row - 1][num:] + nums[row - 1][0:num]
#     else:
#         nums[row - 1] = nums[row - 1][-num:] + nums[row - 1][0:-num]

for i in lst:
    row, dir, num = i
    if dir == 0:
        for _ in range(num):
            nums[row - 1].append(nums[row - 1].pop(0))
    else:
        for _ in range(num):
            nums[row - 1].insert(0, nums[row - 1].pop())

# 모래시계 영역 더하기
start = 0
end = N-1
for i in range(N):
    for j in range(start, end+1):
        result += nums[i][j]

    if i < N//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(result)
