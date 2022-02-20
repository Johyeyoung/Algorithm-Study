#인접행렬

n,m = map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)]

#무방향일때 가중치 없을때
for i in range(m):
    a, b= map(int, input().split())
    g[a][b] = 1 
    g[b][a] = 1

#방향그래프일때 가중치가 있을때
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c


for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()