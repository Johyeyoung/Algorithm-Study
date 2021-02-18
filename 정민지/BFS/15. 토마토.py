import sys
from collections import deque

#sys.stdin = open("input.txt", "r")

# 강의 풀이
if __name__ == '__main__':
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    m, n = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    res = [[0]*m for _ in range(n)]
    q = deque()
    result = 0

    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1:
                q.append((i, j))

    while q:
        y, x = q.popleft()

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            if (0 <= new_y < n) and (0 <= new_x < m) and lst[new_y][new_x] == 0:
                lst[new_y][new_x] = 1
                q.append((new_y, new_x))
                res[new_y][new_x] = res[y][x] + 1
                if result < res[new_y][new_x]:
                    result = res[new_y][new_x]

    # 토마토가 익지 못하는 상황
    # 현재 lst에는 안익은 토마토가 익을 수 있는 경우 1로 바뀐 상태가 저장되어 있음
    # => lst에 0이 있다면 토마토가 익지 못하는 상황임
    flg = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0:
                flg = 1

    if flg == 1:
        print(-1)
    else:
        print(result)