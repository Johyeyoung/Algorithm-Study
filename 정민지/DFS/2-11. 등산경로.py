import sys

#sys.stdin = open("input.txt", "r")

def DFS(y, x):
    global cnt
    visited[y][x] = 1

    if (end_y == y) and (end_x == x):
        cnt += 1

    else:
        for i in range(4):
            newY = y + dy[i]
            newX = x + dx[i]
            if (0 <= newY < n) and (0 <= newX < n):
                if lst[y][x] < lst[newY][newX]:
                    if visited[newY][newX] == 0:
                        visited[newY][newX] = 1
                        DFS(newY, newX)
                        visited[newY][newX] = 0


if __name__ == '__main__':
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    n = int(input())
    cnt = 0
    lst = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    bottom, top = lst[0][0], lst[0][0]
    start_y, start_x = 0, 0
    end_y, end_x = 0, 0

    for i in range(n):
        for j in range(n):
            if lst[i][j] < bottom:
                bottom = lst[i][j]
                start_y, start_x = i, j

            elif top < lst[i][j]:
                top = lst[i][j]
                end_y, end_x = i, j

    DFS(start_y, start_x)
    print(cnt)















