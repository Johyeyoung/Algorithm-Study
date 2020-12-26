## 알리바바와 40인의 도둑 (Bottom-Up)

# 최단거리 유형과 비슷함

import sys
sys.stdin = open("input.txt", 'r')    


#입력값 받음
if __name__=="__main__":
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]  
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=arr[0][0] 


#표의 가장자리
    for i in range(1, n):
        dy[0][i]=dy[0][i-1]+arr[0][i] 
        dy[i][0]=dy[i-1][0]+arr[i][0]

#가는 방법이 2개인 경우
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]
    
    
    
    print(dy[n-1][n-1])