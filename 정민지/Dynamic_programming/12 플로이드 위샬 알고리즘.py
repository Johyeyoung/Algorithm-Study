import sys

# ** 플로이드-워샬 알고리즘 : 최단 경로 문제

# 강의 풀이
# sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
d = [[float('inf')] * (N+1) for _ in range(N+1)]  # d[i][j] : i노드에서 j노드까지 가는 최소 비용

# d 배열 대각선 0으로 초기화(자기 자신으로 가는 경로)
for i in range(N+1):
    d[i][i] = 0

# 문제에서 주어진 노드 간 비용 d에 저장
for i in range(M):
    node1, node2, cost = map(int, input().split())
    d[node1][node2] = cost

# 최소 비용 찾기
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])   # i -> j 비용 vs i -> k -> j 비용

for i in range (1, N+1):
    for j in range(1, N+1):
        if d[i][j] == float('inf'):
            print("M", end=' ')
        else:
            print(d[i][j], end=' ')
    print()


