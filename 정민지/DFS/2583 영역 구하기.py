import sys

#sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)

def DFS(y, x):
    global cnt

    if visited[y][x] == 1:
        return

    visited[y][x] = 1
    cnt += 1

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if (0 <= new_y < n) and (0 <= new_x < m):
            if board[new_y][new_x] == 0:
                DFS(new_y, new_x)



if __name__ == "__main__":
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    n, m, k = map(int, input().split())
    result = []
    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for i in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for x in range(x1, x2):
            for y in range(y1, y2):
                board[y][x] = 1


    for i in range(n):
        for j in range(m):
            cnt = 0
            if board[i][j] == 0 and visited[i][j] == 0:
                DFS(i, j)
                result.append(cnt)

    result.sort()
    print(len(result))
    for i in range(len(result)):
        print(result[i], end=' ')
