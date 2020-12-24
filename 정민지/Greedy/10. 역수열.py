import sys

# sys.stdin = open("input.txt", "rt")
N = int(input())
lst = list(map(int, input().split()))
result = [0] * (len(lst) + 1)

for i in range(N):
    cnt = lst[i]
    idx = 0
    if cnt == 0:    #1. lst의 값이 0인 경우 result배열에서 처음으로 값이 0인 idx에 집어넣음
        for j in range(N):
            if result[j] == 0:
                result[j] = i + 1
                break
    else:   #2. lst의 값이 0이 아닌 경우 result에서 cnt만큼 0의 개수 찾아서 idx에 값 넣어야 함
        while cnt > 0:
            if result[idx] == 0:
                cnt -= 1
            idx += 1    # idx = result에 들어갈 위치

        if result[idx] == 0:    # 2-1 result에 들어갈 위치에 0이 있을 경우 그냥 넣음
            result[idx] = i + 1
        else:   # 2-2 result에 들어갈 위치에 0이 없을 경우 그 뒤에 넣어야 함
            while result[idx] != 0:
                idx += 1
            result[idx] = i + 1
        # print("idx: ", idx, " i+1: ", i+1)
    # print(result)

# 강의 풀이
# for i in range(N):
#     for j in range(N):
#         if lst[i] == 0 and result[j] == 0:
#             result[j] = i + 1
#             break
#         elif result[j] == 0:
#             lst[i] -= 1

for i in range(N):
    print(result[i], end=' ')












