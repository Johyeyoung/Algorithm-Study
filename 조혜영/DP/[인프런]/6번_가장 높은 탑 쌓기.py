
#-------------------------------------------------------------

# Bottom-up & greedy(Ascending By 면적)

#-------------------------------------------------------------


n=int(input())
bricks=[]
for i in range(n):
    a, b, c=map(int, input().split())
    bricks.append((a, b, c))
    
#-------------------------------------------------------------
# greedy처럼 벽돌의 면적을 기준으로 오름차순으로 정렬하여 (기준: 면적)
# 총 3가지의 조건, 면적, 높이, 무게의 3가지 변수 중 하나를 제거
bricks.sort(reverse=True)
# dy[i]는 i번째 벽돌을 최상단에 두었을때 쌓을 수 있는 max높이
dy=[0]*n 
dy[0]=bricks[0][1]

# dp배열을 채우면서 끝내는 것이 아니라 가장 큰 dp의 값을 구해야됨 (answer)
res=bricks[0][1];

# 벽돌수만큼 반복하면서 dp를 채운다.
for i in range(1, n):
    max_h=0;
    
    
    # 자신 앞에 있는 자기보다 면적이 큰 벽돌을 조회하면서 무게가 더 무거운 벽돌이 발견되면 
    # 해당 벽돌의 높이들을 확인하면서 가장 큰 높이를 가지고 있는 면적의 높이의 dy[j]에 자신의 높이를 쌓아올린다.
    for j in range(i-1, -1, -1):
        if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
            max_h=dy[j]
    dy[i]=max_h+bricks[i][1] # dp 배열을 update
    
    res=max(res, dy[i]) # 전체 중에 가장 큰 높이의 결과를 찾기
print(res)
