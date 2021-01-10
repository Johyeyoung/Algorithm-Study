#     2차원 배열 -> 리스트 안에 리스트

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                      7번. 사과나무 (2차원 배열)
#            (범위 설정) largest : 조건을 만족하는 가장 큰 랜선의 길이
#…………………………………………………………………………………………………………………………………………………………………………………………

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2 # s 시작, e 끝


# 2차원 배열 -> 2중 for문
for i in range(n):

    # 한 행에서 다루는 구간 0~n이 아니라 s~e까지만 	
    for j in range(s, e+1): 
        res+=a[i][j]
    if i<n//2: # 구간 넓히기 
        s-=1
        e+=1
    else: # 구간 좁히기
        s+=1
        e-=1
print(res)







#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                        8번. 곳감 (2차원 배열)
#            (범위 설정) largest : 조건을 만족하는 가장 큰 랜선의 길이
#…………………………………………………………………………………………………………………………………………………………………………………………
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k=map(int, input().split())
    if(t==0):
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)






#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                     9번. 봉우리 (2차원 배열)
#            (범위 설정) largest : 조건을 만족하는 가장 큰 랜선의 길이
#…………………………………………………………………………………………………………………………………………………………………………………………

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

# 가장자리 0으로 초기화 setting
a.insert(0, [0]*n) # 0번 행에 넣어라 
a.append([0]*n) # 맨 밑의 행에 넣어라
for x in a: # 모든 행에 대해 좌, 우 채우기!!
    x.insert(0, 0)
    x.append(0)

# 이제부터 2차원 배열, 2중 for문 돌면서 
cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):  
            cnt+=1
print(cnt)
