import sys

#sys.stdin = open("input.txt", "rt")

# DFS(x) : x가 원소로 들어간다 vs 들어가지 않는다
# 나의 풀이
def DFS(x):
    if x == n:
        s1, s2 = 0, 0
        for i in range(len(ch)-1):
            if ch[i] == 1:  # 부분집합1
                s1 += lst[i]
            else:           # 부분집합2
                s2 += lst[i]
        if s1 == s2:
            print("YES")
            sys.exit(0) # 프로그램 전체 종료

    else:
        ch[x] = 1   # 원소 사용함
        DFS(x+1)
        ch[x] = 0   # 원소 사용하지 않음
        DFS(x+1)

# 강의 풀이
total = sum(lst)
def DFS2(L, sum):   # L : lst의 인덱스, sum : 원소 더한 값
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS2(L+1, sum + lst[L]) # 원소 사용함
        DFS2(L+1, sum)  # 원소 사용하지 않음


if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    ch = [0] * (n+1)    # 원소 사용했는지 안 사용했는지 체크
    DFS(0)
    print("NO")











