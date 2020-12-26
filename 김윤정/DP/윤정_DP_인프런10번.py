## 동전교환(냅색알고리즘)

#dy[j] : j원을 거슬러 주는데 사용된 동전의 최소 개수
#dy를 초기화할때 문제에서 최소값을 찾기때문에 큰값으로 초기화한다. 여기서는 거스름돈이 최대 500원이니까 1000정도로 해주자.
#원리는 9번 문제와 같음

import sys
sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n=int(input())
    coin=list(map(int, input().split()))
    m=int(input())
    dy=[1000]*(m+1)
    dy[0]=0

    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j]=min(dy[j], dy[j-coin[i]]+1)

    print(dy[m])