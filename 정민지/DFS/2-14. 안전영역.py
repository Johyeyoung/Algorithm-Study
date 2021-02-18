import sys

#sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

# 강의 풀이
def DFS(y, x, h):
    if visited[y][x] == 1:
        return

    visited[y][x] = 1

    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if (0 <= newY < n) and (0 <= newX < n):
            if lst[newY][newX] > h:
                DFS(newY, newX, h)


if __name__ == '__main__':
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    cnt = 0
    res = 0
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    for h in range(100):
        visited = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0 and h < lst[i][j]:
                    cnt += 1
                    DFS(i, j, h)

        if res < cnt:
            res = cnt

        if cnt == 0:
            break

    print(res)


