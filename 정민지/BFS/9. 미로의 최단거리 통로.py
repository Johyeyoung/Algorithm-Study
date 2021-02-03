import sys
from collections import deque

#sys.stdin = open("input.txt", "r")
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n = 7
lst = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dis = [[0] * n for _ in range(n)]
dq = deque()
dq.append((0, 0))
while dq:
    front = dq.popleft()
    for i in range(4):
        nextY = front[0]+dy[i]
        nextX = front[1]+dx[i]
        if (0 <= nextY < n) and (0 <= nextX < n):
            #print(front[0] + dy[i], ", ", front[1]+dx[i])
            if visited[nextY][nextX] == 0:
                if lst[nextY][nextX] == 0:
                    visited[nextY][nextX] = 1
                    dis[nextY][nextX] = dis[front[0]][front[1]] + 1
                    if nextY == n-1 and nextX == n-1:
                        break
                    else:
                        dq.append((nextY, nextX))

if dis[n-1][n-1] == 0:
    print(-1)
else:
    print(dis[n-1][n-1])
















