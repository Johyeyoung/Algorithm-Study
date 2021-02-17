import sys

#sys.stdin = open("input.txt", "r")

def DFS(y, x):
    global cnt

    if visited[y][x] == 1:
        return

    cnt += 1
    visited[y][x] = 1

    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if (0 <= newY < n) and (0 <= newX < n):
            if lst[newY][newX] != 0:
                lst[newY][newX] = num
                DFS(newY, newX)


if __name__ == '__main__':
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    n = int(input())
    cnt = 0
    num = 0
    lst = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            cnt = 0
            if (lst[i][j] == 1) and (visited[i][j] == 0):
                num += 1
                DFS(i, j)
                result.append(cnt)

    print(len(result))
    result.sort()
    for i in range(len(result)):
        print(result[i])
















