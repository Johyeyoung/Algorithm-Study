import sys

#sys.stdin = open("input.txt", "rt")

# 나의 풀이 -> 시간초과
# L : 남은 거슬러 줄 금액 => 0원이 되면 종료
# re : 거슬러 줄 동전의 최소 개수가 될 수 있는 경우의 수
def DFS(L, re):
    global cnt
    if cnt < re:    # 강의 보고 추가함
        return

    if L < 0:
        return

    if L == 0:
        if re < cnt:
            cnt = re

    else:
        for i in range(n):
            DFS(L-coins[i], re+1)


# L : 거슬러 줄 동전의 개수
# sum : 동전의 합
def DFS2(L, sum):
    global res
    if res < L:
        return

    if m < sum:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS2(L+1, sum+coins[i])

if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort(reverse=True)
    m = int(input())
    cnt = float('inf')
    res = float('inf')
    DFS(m, 0)
    DFS2(0, 0)
    # print(res)
    print(cnt)

















