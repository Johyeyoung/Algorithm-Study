## 가장 높은 탑 쌓기(LIS 응용)

#사이즈는 큰거가 아래, 작은게 위에
#무게는 무거운게 아래, 가벼운게 위에


n=5

bricks=[(25,3,4),(16,2,5),(9,2,3),(4,4,6),(1,5,2)]

dy=[0]*n

dy[0]=bricks[0][1]
res=bricks[0][1]

for i in range(1,n):
    max_h=0
    for j in range(i-1, -1, -1):
        if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
            max_h=dy[j]
        dy[i]=max_h+bricks[i][1]
        res=max(res, dy[i])
print(res)
