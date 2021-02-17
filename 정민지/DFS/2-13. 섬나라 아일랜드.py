import sys

#sys.stdin = open("input.txt", "r")

def DFS(y, x):
    if visited[y][x] == 1:
        return

    visited[y][x] = 1

    for i in range(8):
        newY = y + dy[i]
        newX = x + dx[i]
        if (0 <= newY < n) and (0 <= newX < n):
            if lst[newY][newX] != 0:
                DFS(newY, newX)


if __name__ == '__main__':
    dy = [-1, 0, 1, 0, -1, -1, 1, 1]
    dx = [0, 1, 0, -1, -1, 1, -1, 1]

    n = int(input())
    cnt = 0
    lst = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (lst[i][j] == 1) and (visited[i][j] == 0):
                DFS(i, j)
                cnt += 1


    print(cnt)
