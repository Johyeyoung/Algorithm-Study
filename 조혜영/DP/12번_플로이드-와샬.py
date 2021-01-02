
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#           12번. 플로이드-와샬 (그래프 최단 거리)
#
#   dy[j]: 가방이 j무게일때 가질 수 있는 보석의 최대 가치
#…………………………………………………………………………………………………………………………………………………………………………………………

n, m=map(int, input().split())
dis=[[5000]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dis[i][i]=0
for i in range(m):
    a, b, c=map(int, input().split())
    dis[a][b]=c
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j]==5000:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()






#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#             13번. 회장뽑기
#
#    dy[j]: j원을 거슬러주는데 사용된 동전의 최소 개수
#…………………………………………………………………………………………………………………………………………………………………………………………

n=int(input())
dis=[[100]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dis[i][i]=0
while True:
    a, b=map(int, input().split())
    if a==-1 and b==-1:
        break
    dis[a][b]=1
    dis[b][a]=1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

res=[0]*(n+1)
score=100
for i in range(1, n+1):
    for j in range(1, n+1):
        res[i]=max(res[i], dis[i][j])
    score=min(score, res[i])
out=[]
for i in range(1, n+1):
    if res[i]==score:
        out.append(i)
print("%d %d" %(score, len(out)))
for x in out:
    print(x, end=' ')







#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#      14번. 위상정렬 (그래프)
#
#…………………………………………………………………………………………………………………………………………………………………………………………

n, m=map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
degree=[0]*(n+1)
dQ=deque()
for i in range(m):
    a, b=map(int, input().split())
    graph[a][b]=1
    degree[b]+=1
for i in range(1, n+1):
    if degree[i]==0:
        dQ.append(i)
while dQ:
    x=dQ.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
        if graph[x][i]==1:
            degree[i]-=1
            if degree[i]==0:
                dQ.append(i)
