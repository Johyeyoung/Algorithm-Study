# [DP] 최대점수 구하기 (냅색 알고리즘)
n=5
m=20

dy=[0]*(m+1)

for i in range(n):
    ps, pt =map(int, input().split())
    for j in range(m, pt-1, -1):
        dy[j]=max(dy[j], dy[j-pt]+ps)
    print(dy[m])
    
