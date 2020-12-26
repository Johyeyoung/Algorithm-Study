##  최대 부분 증가수열(DP)


#각 숫자가 내가 만들고자하는 수열의 가장 마지막에 들어갔을때
#만들 수 있는 가장 긴 증가수열

arr=[5,3,7,8,6,2,9,4]
arr.insert(0,0)
n=8
dy=[0]*(n+1)
res=0

dy[1]=1

print(arr)

for i in range(2,n+1):
    max=0
    for j in range(i-1, 0,-1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]

print(res)




