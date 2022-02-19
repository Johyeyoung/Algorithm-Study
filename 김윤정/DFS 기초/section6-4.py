#합이 같은 부분집합
#L은 a list의 인덱스 번호

import sys

def DFS(L, sum):
    if L==n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
        else:
            DFS(L+1, sum+a[L])
            DFS(L+1, sum)



if __name__ =="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total = sum(a)
    DFS(0,0)
    print("NO")