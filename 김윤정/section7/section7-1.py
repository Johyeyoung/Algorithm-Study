# 최대점수 구하기


def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L==n:
        if sum > res:
            res=sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])#문제 풀었을떼
        DFS(L+1, sum, time) #문제 안풀었을떼

if __name__ == '__main__':
    n,m = map(int, input().split())
    pv=list()
    pt=list()
    for i in range(n):
        a, b= map(int, input().split())
        pv.append(a)
        pt.append(b)
    res=-2147000000
    DFS(0,0,0)