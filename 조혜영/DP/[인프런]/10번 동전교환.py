# 동전교환 DFS (중복조합)

 def dfs(sum_, i, cnt):  # 중복순열이 되는 것을 막기위해 index정보인 i를 가지고 다님 
    global min_cnt
    
    if cnt >= min_cnt or sum_ > m: return  # 불필요한 재귀방지
    
    if sum_ == m:  # 탈출조건
        if min_cnt > cnt: min_cnt = cnt
        return
    else:
        for idx in range(i, len(coins)):
            dfs(sum_+coins[idx], idx, cnt+1)


if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    m=int(input())
    min_cnt=2147000000
    coins.sort(reverse=True)  #깊이 들어가는거 방지
    DFS(0, 0, 0)
    print(min_cnt)


# DP

mport sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n=int(input())
    coin=list(map(int, input().split()))
    m=int(input())
    dy=[1000]*(m+1);
    dy[0]=0
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j]=min(dy[j], dy[j-coin[i]]+1)
    print(dy[m])


# 다이나믹 방법은 모든 원소가 다 주어지는게 아닌 하나씩만 주어졌다고 생각하고 하나씩 채워가야됨 Bottom-up
# 점화식을 세울 수 있다면 dp -> 점화식이라면 이전에 구한 값을 이용한다는 소리임 

n=int(input()) 
coin=list(map(int, input().split())) 
m=int(input()) 

dy=[1000]*(m+1) # dp배열 선언 (dy[j]: j원을 거슬러주는데 사용된 동전의 최소 개수)
dy[0]=0

# 동전의 종류(n개)별로 dy를 순회하면서 최소 개수를 update시킨다.
for i in range(n): 
    for j in range(coin[i], m+1):  # 돌려줘야할 거스름돈(j)이 해당 동전보다는 큰 경우만 update  
        dy[j]=min(dy[j], dy[j-coin[i]]+1) # 최소값을 선택하는거니까 min
print(dy[m])


for i in range(n): 
    ###for j in range(coin[i], m+1):  # 돌려줘야할 거스름돈(j)이 해당 동전보다는 큰 경우만 update  
        dy[j]=min(dy[j], dy[j-coin[i]]+1) # 최소값을 선택하는거니까 min

이렇게 점화식을 dy[j]가 정의될 수 있는게 한번이 아닌 여러번(for_)인 상황인게 차이 - 징검다리 문제의 보폭이 여기선 동전인거임 





# 시간 복잡도  : 중복순열 > 중복조합 > dP
