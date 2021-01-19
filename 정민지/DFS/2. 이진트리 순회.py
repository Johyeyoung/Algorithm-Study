import sys

sys.stdin = open("input.txt", "rt")
n = int(input())

# 1. 전위 순회 (깊이 우선 탐색)
def DFS(x):
    if x > n:
        return
    else:
        print(x, end=' ')
        DFS(x * 2)  # 왼쪽 노드 방문 (2, 4 ...)
        DFS(x * 2 + 1)  # 오른쪽 노드 방문 (3, 5, ...)

# 2. 중위 순회 ( 왼 - 부모 - 오른 )
def DFS(x):
    if x > n:
        return
    else:
        DFS(x * 2)  # 왼쪽 노드 방문 (2, 4 ...)
        print(x, end=' ')
        DFS(x * 2 + 1)  # 오른쪽 노드 방문 (3, 5, ...)

# 후위 순회 ( 왼 - 오른 - 부모 )
def DFS(x):
    if x > n:
        return
    else:
        DFS(x * 2)  # 왼쪽 노드 방문 (2, 4 ...)
        DFS(x * 2 + 1)  # 오른쪽 노드 방문 (3, 5, ...)
        print(x, end=' ')


if __name__ == "__main__":
    DFS(1)













