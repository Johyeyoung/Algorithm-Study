import sys

# ** 위상정렬
# - 진입차수 : 노드로 들어오는 간선의 개수
# 풀이 순서
# 1. 그래프 만들면서 진입 차수 배열 만들기
# 2. 큐 활용하여 진입 차수가 0인 노드를 넣음과 동시에 해당 노드가 만드는 진입 차수의 배열값 1감소시킴
# 3. 큐에서 노드 꺼냄

# 강의 풀이
sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
degree = [0] * (N+1)    # degree[idx] : idx노드로 들어오는 간선의 개수
graph = [[0] * (N+1) for _ in range(N+1)]  # graph[i][j] : i -> j 가리키면 1, 없으면 0
q = []

# 1. 그래프 만들기, 진입 차수 배열 만들기
for i in range(N):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    degree[node2] += 1

# 2. 큐에 진입 차수가 0인 노드 넣기
for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

# 3.
while len(q) != 0:
    now = q.pop(0)
    print(now, end=" ")     # 큐에서 노드 꺼내고

    for i in range(1, N+1):     # 해당 노드가 만드는 진입 차수의 배열값 1감소시킴
        if graph[now][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:      # 다시 진입 차수 값이 0이면 큐에 넣기
                q.append(i)