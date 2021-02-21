import sys

#sys.stdin = open("input.txt", "r")

# 강의 풀이
# 1. 처음 주어진 피자집의 개수Cm (조합)을 구한다. -> 이때 DFS사용함
# 2. 위에서 구한 경우의 수 모두 계산한다. 이 중 최소 거리를 구한다.
# => 정답이 될 수 있는 경우의 수(남는 피자 가게의 경우의 수) 구한 후 집과의 거리 계산 후 최솟값을 갱신함

def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for i in range(len(house)):
            y1 = house[i][0]
            x1 = house[i][1]
            dis = 21470000000
            for x in cb:
                y2 = pizza[x][0]
                x2 = pizza[x][1]
                dis = min(dis, abs(x1-x2) + abs(y1-y2))
            sum += dis  # 한 가지 경우의 피자 거리의 값

        if sum < res:
            res = sum   # 최솟값을 찾기 위함

    else:
        for i in range(s, len(pizza)):
            cb[L] = i
            DFS(L+1, i+1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    house = []  # 집의 좌표 저장
    pizza = []  # 피자집의 좌표 저장
    cb = [0] * m   # 남는 피자집의 경우의 수
    res = float('inf')

    for i in range(n):
        for j in range(n):
            if lst[i][j] == 1:
                house.append((i, j))

            elif lst[i][j] == 2:
                pizza.append((i, j))
    DFS(0, 0)
    print(res)


