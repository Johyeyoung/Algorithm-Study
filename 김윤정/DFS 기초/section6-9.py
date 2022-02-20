#수열 추측하기(순열, 파스칼 응용)
import sys

def DFS(L, sum):
    if L==n and sum ==f:
        for x in p:
            print(x, end='  ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

if __name__ == '__main__':
    n=4
    f=16
    p=[0]*n
    b=[1]*n  #이항계수의 맨끝은 다 1이기때문에 1로 초기화
    ch=[0]*(n+1)
    for i in range(1, n):
        b[i]=b[i-1]*(n-i)//i  #조합 이항계수 계산
    DFS(0,0)
