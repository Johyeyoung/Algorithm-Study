#동전교환

from pickletools import read_unicodestring4


def DFS(L, sum):
    global res
    #합이 구하려는 값보다 커지면 더이상 구할 필요없기때문에 
    if sum > m :
        return 
    #L이 res보다 커지면 구할 필요가 없음
    if L >res :
        return
    if sum == m:
        if L <res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])
            

if __name__ == '__main__':
    n=int(input())
    a=list(map(int, input().split()))
    m=int(input())
    res = 2147000000 #최소값 찾기위해 
    a.sort(reverse=True) #가장 큰 수부터 정렬
    DFS(0,0)
    print(res)