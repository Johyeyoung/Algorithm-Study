# [DP] 플로이드-와샬(그래프최단거리)

#그래프에서 모든 정점에서 모든 정점까지 가는 최단 거리


n,m = map(int, input().split())
dis=[[5000]*(n+1) for _ in range(n+1)]

#출발지와 도착지가 같은 경우를 0으로 초기화한것
for i in range(1, n+1):
    dis[i][i]=0
#i->j 직행했을때
for i in range(m):
    a,b,c=map(int, input().split())
    dis[a][b]=c

#플로이드-와샬 (중요)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

for i in range(1, n+1):
    for j in range(1,n+1):
        if dis[i][j]==5000:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()





