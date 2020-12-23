import sys

# sys.stdin = open("input.txt", "rt")
N = int(input())
information = []
check = [0] * (N+1)
cnt = N

for i in range(N):
    information.append(list(map(int, input().split())))

# 다른 지원자와 비교했을 때 키와 몸무게 모두가 작은 지원자 X
for i in range(len(information)):
    for j in range(len(information)):
        if i == j:
            continue
        else:
            # print("h", information[j][0], " ", information[i][0])
            # print("w", information[j][1], " ", information[i][1])
            if (information[i][0] < information[j][0]) & (information[i][1] < information[j][1]):
                cnt -= 1
                break

print(cnt)










