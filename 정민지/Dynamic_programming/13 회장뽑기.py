import sys

# ** 무방향 그래프 문제
# 강의 풀이
# sys.stdin = open("input.txt", "rt")
N = int(input())
res = [0] * (N+1)
d = [[float('inf')] * (N+1) for _ in range(N+1)]  # d[i][j] : i노드에서 j노드까지 가는 최소 비용

# d 배열 대각선 0으로 초기화(자기 자신으로 가는 경로)
for i in range(N+1):
    d[i][i] = 0

# 문제에서 주어진 노드 간 비용 d에 저장
id1, id2 = 0, 0
while (id1 != -1) and (id2 != -1):
    id1, id2 = map(int, input().split())
    d[id1][id2] = 1
    d[id2][id1] = 1     # 주의!! 양방향 그래프 문제이므로 초기화를 양방향으로 해야 함

# 친구 찾기
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])   # i -> j 비용 vs i -> k -> j 비용

# for i in range (1, N+1):
#     for j in range(1, N+1):
#         if d[i][j] == float('inf'):
#             print("M", end=' ')
#         else:
#             print(d[i][j], end=' ')
#     print()
score = 100
for i in range(1, N+1):
    for j in range(1, N+1):
        res[i] = max(res[i], d[i][j])
    score = min(score, res[i])

out = []
for i in range(1, N+1):
    if res[i] == score:
        out.append(i)

print(f"{score} {len(out)}")
for i in range(len(out)):
    print(out[i], end=' ')

