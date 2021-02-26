
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#             12번. 플로이드-와샬 (그래프 최단 거리)
# 
#     모든 정점에서 정점 사이의 최단 거리를 구하기위해 2차원 tabel을 생성 
#     이때 순서는 상관없음 (오름,내림x) / 중복가능 최소거리만 나오면 됨
#……………………………………………………………………………………………………………………………………………………………………………………………………………

n, m=map(int, input().split())


# -------------------- 플로이드-와샬 정보 채우기 --------------------------

# dis - 1) 플로이드-와샬을 위해 2차원 table을 생성한다 
#          이때 max_limit로 채우기 (최소거리로 update할꺼라서)
dis=[[5000]*(n+1) for _ in range(n+1)]

# dis - 2) 자기자신은 거리 0으로 기본 초기화
for i in range(1, n+1):
    dis[i][i]=0
    
# dis - 3) direct로 연결된 정점 사이의 초기화: 직접 연결됐을 때 발생하는 cost기입
for i in range(m):
    a, b, c=map(int, input().split()) # a와 b는 직접 연결되어있고 c만큼의 비용生
    dis[a][b]=c
    
# dis - 4) 나머지 undirect한 정점사이의 최단 거리 구해서 채우기  

# i -> j까지의 경로에서 K를 지나간 i -> K -> j 일때의 경로가 더 최소 cost인지 확인후 update!
for k in range(1, n+1): # 모든 k를 하나하나 다 지나간다고 가정하니까 Knapsack!!
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 두 정점 사이의 연결 i -> j와 i -> K -> j인 경우 중 최소 cost를 선택!
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
          
        
        
# ---------------- 정답 출력 ---------------------
for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j]==5000:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()






#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                          13번. 회장뽑기
#
#          각 사람과 사람 사이의 최단 거리 구하기 (2차원 tabel) 
#……………………………………………………………………………………………………………………………………………………………………………………………………………

n=int(input()) # 사람의 수 



# -------------------- 플로이드-와샬 정보 채우기 --------------------------

# dis - 1) 플로이드-와샬을 위해 2차원 table을 생성한다 
#          이때 max_limit로 채우기 (최소거리로 update할꺼라서)
dis=[[100]*(n+1) for _ in range(n+1)]

# dis - 2) 자기자신은 거리 0로 기본 초기화
for i in range(1, n+1):
    dis[i][i]=0  
    
# dis - 3) direct로 연결된 정점 사이의 초기화: 각 사람별 친한 사람 정보 받아서 거리 1로 표시하기
while True:  
    a, b=map(int, input().split())
    if a==-1 and b==-1:
        break
    dis[a][b]=1
    dis[b][a]=1
    
# dis - 4) 나머지 undirect한 정점사이의 최단 거리 구해서 채우기    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 두  사이의 연결 i -> j와 i -> K -> j인 경우 중 최소 cost를 선택!
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j]) 
            
            
            
            
# -------------------------- 정답 출력 ----------------------------------
# 각 사람(:행 단위)이 가지고 있는 점수들 중에서 최대 점수를 기록한다 (1번 사람 -> res[1]에 최대점수 기록)            
res=[0]*(n+1)
score=100 # 최대 점수들 중 가장 작은값을 기록하여 후보가 될 점수를 기록
for i in range(1, n+1):
    for j in range(1, n+1):
        res[i]=max(res[i], dis[i][j]) # 각자 가진 최대점수를 기록 
    score=min(score, res[i]) # 최대점수 중 가장 작은 값을 기억한다. (후보가 될 점수)
    

out=[]
for i in range(1, n+1): 
    if res[i]==score:
        out.append(i)
print("%d %d" %(score, len(out))) # 후보의 점수와 후보 수
for x in out: # 후보들 번호 출력
    print(x, end=' ')






    
    
