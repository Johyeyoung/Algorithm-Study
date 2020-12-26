import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)

#------------------------------------------------
# bottom up용 list 배열 선언하고
dy=[0]*(n+1)
dy[1]=1 # 직관적으로 1번은 최대증가수열이 자기뿐


#------------------------------------------------
res=0
for i in range(2, n+1):  # 1번은 알았으니까 그 다음 2번부터 dy채우기
    
    
    '''
    bottom-up 특성상 앞의 정보 이용하는데
    앞의 index가 가지고 있는 숫자가 본인이 가진 숫자보다 크면 증가 수열이 안됨
    ←방향으로 검사하면서 본인이 가진 수보다 작은 애를 가진 index를 찾아 후보를 생성하고
    해당 index의 dy값 중 가장 큰 증가수열의 값을 가진 애한테 빌붙기
    '''
    max=0
    for j in range(i-1, 0, -1): # ←방향으로 검사
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1 # 가장 큰 증가수열의 값을 가진 애한테 자기몫인 +1하고 기록! 
    # 지금까지는 기록이지 정답이 아님!!!!
    
    # 왜? 해당 마지막항이 꼭 포함되어야 최대 증가수열이 되는 것이 아님 
    # 그전에 이미 더 큰 최대 증가 수열이 있을 수 있으므로 dy내부에서도 경쟁해서 가장 큰거 도출
    if dy[i]>res:
        res=dy[i]
        
print(res)
