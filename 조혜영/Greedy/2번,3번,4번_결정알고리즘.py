
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                            2번. 랜선자르기
#
#              largest : 조건을 만족하는 가장 큰 랜선의 길이
#…………………………………………………………………………………………………………………………………………………………………………………………


# ---------------------------- 정보 입력받기 ---------------------------
k, n=map(int, input().split()) # k: 랜선의 종류/ n: 나와야할 최소 랜선의 조각수 
Line=[] # 주어진 랜선의 종류
res=0
largest=0

# for문으로 가지고 있는 랜선의 정보를 입력받아서 Line에 넣기
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)  # 가장 크게 나올 수 있는 랜선크기
# ----------------------------------------------------------------------

# 해당 길이(len)의 랜선으로 잘랐을때 나올 수 있는 조각의 개수 
def Count(len):
    cnt=0 
    for x in Line:
        cnt+=(x//len)
    return cnt
    
# n조각이상이 나올 수 있는 조건을 만족하되, 가장 최대의 랜선길이를 구해야됨    
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    
    # 랜선의 개수가 기준치보다 많으면 랜선의 길이를 더 늘려도 됨(lt=mid+1)
    if Count(mid)>=n:
        res=mid  # 일단 정답이 범위에는 들었음 하지만 최대를 찾기위해 계속 저장
        lt=mid+1
    # 조각난 랜선의 개수가 기준치보다 적으면 랜선의 길이를 더 줄여야됨 (rt=mid-1)
    else:
        rt=mid-1
print(res)






#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#      3번. 뮤직비디오 (결정알고리즘)
#
#…………………………………………………………………………………………………………………………………………………………………………………………
def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))
maxx=max(Music)
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)






#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#      4번. 마구간 정하기
#
#…………………………………………………………………………………………………………………………………………………………………………………………

def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)


