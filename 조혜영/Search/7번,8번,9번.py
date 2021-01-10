#     2차원 배열 -> 리스트 안에 리스트
# map이 한줄(5 6 7 8)을 읽어서 공백단위로 분리하여 리스트로 만드는 것 [5, 6, 7, 8] 
# a=[list(map(int, input().split())) for _ in range(n)]


#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                  6번. 격자판 최대합 (2차원 배열)
#                  (행탐색 + 열탐색 + 대각선탐색)
#…………………………………………………………………………………………………………………………………………………………………………………………


n=int(input())
# -------------2차원 배열만들기---------------
a=[list(map(int, input().split())) for _ in range(n)]
largest=-2147000000
# 1.....행과 열 확인하기
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]  # 열 check
        sum2+=a[j][i]  # 행 check  

   # 가장 큰 행이나 열있는지 기록  
   if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
# 2.....대각선도 확인하기
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]   # 좌측 대각선 check
    sum2+=a[i][n-i-1]   #  우측 대각선 check
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)






#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                      7번. 사과나무 (2차원 배열 - 다이아몬드형)
#        2차원 전체탐색이 아닌 부분 탐색 - 지정된 행 내부의 모든 원소가 아닌 특정 부분만 check
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
    # 전반 행까지 가는 동안 범위 증가하다가 후반 행부터는 범위 감소
    if i<n//2: # 구간 넓히기 
        s-=1
        e+=1
    else: # 구간 좁히기
        s+=1
        e-=1
print(res)







#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                        8번. 곳감 (2차원 배열 - 모래시계형 + 배열  )
#         2차원 전체탐색이 아닌 부분 탐색 - 지정된 행 내부의 모든 원소가 아닌 특정 부분만 check
#…………………………………………………………………………………………………………………………………………………………………………………………
n=int(input())
# ---------------2차원 배열만들기---------------
a=[list(map(int, input().split())) for _ in range(n)]
# -------------m번만큼 배열 수정하기---------------
m=int(input())
for i in range(m):
    # h: target 행, t: 방향, k: k번만큼 이동
    h, t, k=map(int, input().split()) # h행에서 1(오른쪽)/0(왼쪽)방향으로 k번만큼 이동
    if(t==0): # 왼쪽으로 이동 ->
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) # 맨 앞에꺼 빼서-pop(0) 맨뒤에 넣기
    else: # 오른쪽으로 이동 <-
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) # 맨 뒤에꺼 빼서-pop() 앞으로 넣기 

res=0
s=0
e=n-1
for i in range(n):
    # 지정된 i행 내부에서 s~e까지의 범위만 check
    for j in range(s, e+1):  
        res+=a[i][j]
    # 전반 행까지 가는 동안 범위 증가하다가 후반 행부터는 범위 감소
    if i<n//2: # 범위 줄이기 
        s+=1
        e-=1
    else: # 범위 늘리기 
        s-=1
        e+=1
print(res)



