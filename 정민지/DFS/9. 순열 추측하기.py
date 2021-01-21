import sys

#sys.stdin = open("input.txt", "rt")

def DFS(L, sum):
    if L == n and sum == f:
        for i in range(len(p)):
            print(p[i], end=' ')
        sys.exit(0)     # 최초로 발견한 한 개의 순열만 출력함
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i+1
                DFS(L+1, sum+p[L]*b[L])
                ch[i] = 0


# 규칙 찾기!!
# 가장 밑에 있는 숫자 구하는 규칙이 있다
# f = p[0] * n-1C0 + p[1] * n-1C1 + p[2] * n-1C2 + ... + p[n-1] * n-1Cn-1
# 1. nC0과 같은 이항계수를 b배열에 담는다
# 2. 가능한 순열(p)를 만든다
# 3. p와 b 배열의 각 인덱스의 합이 f와 같다면 break

if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n # 순열 (답이 될 수 있는 경우의 수)
    b = [1] * n # 이항계수(n-1C0, n-1C1, n-1C2, ... n-1Cn-1)
    ch = [0] * n
    # b배열 만들기(이항계수 만들기)
    for i in range(1, n-1):    # b[0]과 b[n-1]은 1이므로 계산할 필요x
        b[i] = ((n-i) * b[i-1]) // i
    DFS(0, 0)





















