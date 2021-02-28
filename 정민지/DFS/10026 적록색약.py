import sys

#sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)

def DFS1(y, x, color):
    global cnt

    if visited[y][x] == 1:
        return

    visited[y][x] = 1

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if (0 <= new_y < n) and (0 <= new_x < n):
            if board[new_y][new_x] == color:
                DFS1(new_y, new_x, color)

def DFS2(y, x, color):
    global cnt

    if visited[y][x] == 1:
        return

    visited[y][x] = 1

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if (0 <= new_y < n) and (0 <= new_x < n):
            if board[new_y][new_x] == 'B':
                if board[new_y][new_x] == color:
                    DFS2(new_y, new_x, color)
            else:
                if color != 'B':
                    DFS2(new_y, new_x, color)



if __name__ == "__main__":
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    n = int(input())
    cnt = 0
    result = []
    board = [list(input()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                DFS1(i, j, board[i][j])
                cnt += 1

    result.append(cnt)

    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                DFS2(i, j, board[i][j])
                cnt += 1
    result.append(cnt)

    for i in range(len(result)):
        print(result[i], end=' ')
