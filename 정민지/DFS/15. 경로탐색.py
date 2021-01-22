import sys


sys.stdin = open("input.txt", "rt")

def DFS(L):
    global cnt
    if L == n:
        cnt += 1
    #print(path)

    else:
        for i in range(1, n+1):
            if lst[L][i] == 1 and ch[i] == 0:
                ch[i] = 1
                ch[L] = 1
                # path.append(i)  // 경로 담는 리스트
                DFS(i)
                ch[i] = 0
                # path.pop()
                ch[L] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    path = [1]
    ch = [0] * (n+1)
    lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        node1, node2 = map(int, input().split())
        lst[node1][node2] = 1

    DFS(1)
    print(cnt)





















