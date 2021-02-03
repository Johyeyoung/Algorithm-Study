import sys

#sys.stdin = open("input.txt", "r")

def DFS(y, x):
    global cnt
    visited[y][x] = 1

    if (y == n-1) and (x == n-1):
        cnt += 1

    else:
        for i in range(4):
            newY = y + dy[i]
            newX = x + dx[i]
            if (0 <= newY < n) and (0 <= newX < n):
                if visited[newY][newX] == 0:
                    if lst[newY][newX] == 0:
                        visited[newY][newX] = 1
                        DFS(newY, newX)
                        visited[newY][newX] = 0


if __name__ == '__main__':
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    n = 7
    cnt = 0
    lst = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    dis = [[0] * n for _ in range(n)]

    DFS(0, 0)
    print(cnt)















