import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")

if __name__ == "__main__":
    n = int(input())
    cnt = 0
    a, b = map(int, input().split())
    m = int(input())
    q = deque()
    visited = [0] * (n+1)
    cnt = [0] * (n+1)
    board = [[] for _ in range(n+1)] # 1.

    for i in range(m):  # 2.
        x, y = map(int, input().split())
        board[x].append(y)
        board[y].append(x)

    q.append(a)
    
    # 3.
    while q:
        now = q.popleft()
        visited[now] = 1
        if now == b:
            break

        for i in range(1, n+1):
            if visited[i] == 0 and now in board[i]:
                q.append(i)
                cnt[i] = cnt[now] + 1

    if cnt[b] == 0:
        print(-1)
    else:
        print(cnt[b])
