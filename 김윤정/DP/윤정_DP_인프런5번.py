## 최대 선 연결하기 - 최대 증가수열의 응용버전 

arr=[4,1,2,3,8,7,5,6,10,8]
arr.insert(0,0)
n=10
dy=[0]*(n+1)
res=0

dy[1]=1

for i in range(2,n+1):
    max=0
    for j in range(i-1, 0,-1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]

print(res)
