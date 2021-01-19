import sys

#sys.stdin = open("input.txt", "rt")

# 강의 풀이
# ** 상태 트리 만들기!!
# DFS(x) : x가 원소로 들어간다 vs 들어가지 않는다

def DFS(x):
    if x == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end='')
        print()

    else:
        ch[x] = 1   # 원소 사용함
        DFS(x+1)
        ch[x] = 0   # 원소 사용하지 않음
        DFS(x+1)

if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1)    # 원소 사용했는지 안 사용했는지 체크
    DFS(1)











