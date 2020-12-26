import sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]  # 맵이 주어지는 부분
    
    
    
    
    # ---------------bottom up용 list 배열 선언하고(최소비용)------------------
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=arr[0][0] # 직관적인 부분(시작부분) 채우고
    
    # --------------for문을 돌면서 목적지 n까지 dy채우기-------------
    # ------------ 올 수 있는 경로가 오직 한가지만 있는 격자점을 먼저 채우고
    for i in range(1, n):
        # build up: 이동하는 방향은 ↓, → 
        dy[0][i]=dy[0][i-1]+arr[0][i] 
        dy[i][0]=dy[i-1][0]+arr[i][0]
    
    # ----------- 해당 격자점으로 올 수 있는 경로가 2가지(→, ↓)인 경우는 최소값에 더해준다
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]
    
    
    
    print(dy[n-1][n-1])
