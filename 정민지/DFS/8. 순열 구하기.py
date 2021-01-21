import sys

#sys.stdin = open("input.txt", "rt")

def DFS(L):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1   # 사용했으면 1로
                res[L] = i
                DFS(L+1)
                ch[i] = 0   # 돌아갈 때 0으로 다시 풀어줌




if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    ch = [0] * (n+1)    # 숫자 사용했는지 안사용했는지 체크
    DFS(0)
    print(cnt)


















