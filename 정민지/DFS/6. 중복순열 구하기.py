import sys

#sys.stdin = open("input.txt", "rt")

# 강의 풀이
def DFS(L): # L : 순열의 인덱스
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):  # 순열 숫자들(1부터 시작)
            res[L] = i  # 순열 채움
            DFS(L+1)    # 인덱스 올림

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m  # 순열들 담을 리스트
    cnt = 0
    DFS(0)
    print(cnt)

















