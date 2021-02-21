import sys

#sys.stdin = open("input.txt", "r")

def DFS(y, x):
    if y == 0:
        print(x)
        sys.exit(0)

    for i in range(3):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if (0 <= new_y < n) and (0 <= new_x < n):
            #print(new_y, " ", new_x)
            if (lst[new_y][new_x] == 1) and (visited[new_y][new_x] == 0):
                visited[y][x] = 1
                DFS(new_y, new_x)


if __name__ == '__main__':
    dy = [0, 0, -1]
    dx = [1, -1, 0]

    n = 10
    lst = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        if lst[9][i] == 2:
            DFS(9, i)


