#순열구하기
#중복순열에서 중복을 허락하지않는 조건만 넣으면됨

def DFS(L):
    global cnt
    if L == m:
        for k in range(L):
            print(res[i], end=" ")
            print()
            cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1   #중복을 피하기위해 ch 리스트에 1로 표시
                res[L]=i
                DFS(L+1)
                ch[i]=0  #다시 돌아왔을때 1로 표시된걸 풀어줘야함

if __name__ == '__main__':
    n,m=map(int, input().split())
    res=[0]*n
    ch=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)