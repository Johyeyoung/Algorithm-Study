# 위상정렬(그래프 정렬)

import sys

sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
degree = [0] * (n+1)    # degree[idx] : idx노드로 들어오는 간선의 개수
graph = [[0] * (n+1) for _ in range(n+1)]  # graph[i][j] : i -> j 가리키면 1, 없으면 0
q = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b] += 1

for i in range(n):
    if degree[i]==0:
        q.append(i)

while len(q) != 0:
    now=q.pop(0)
    q.pop()
    print(now, end=' ')
    for i in range(1,n):
        if graph[now][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)
