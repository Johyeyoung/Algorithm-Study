import sys

# sys.stdin = open("input.txt", "rt")
N = int(input())
time_lst = []
cnt = 1

for i in range(N):
    time_lst.append(list(map(int, input().split())))

# 끝나는 시간이 가장 빠른 회의 기준으로 정렬
time_lst.sort(key=lambda x:x[1])
# print(time_lst)

start = time_lst[0][0]
end = time_lst[0][1]

for i in range(1, len(time_lst)):
    if end <= time_lst[i][0]:   # 이전 회의의 끝나는 시간보다 다음 회의의 시작 시간이 더 커야함
        cnt += 1
        start = time_lst[i][0]
        end = time_lst[i][1]

print(cnt)







