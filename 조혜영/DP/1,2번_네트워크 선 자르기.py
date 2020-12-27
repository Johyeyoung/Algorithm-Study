

# ----------------------------------------------------------
#                   Bottom - up 
# ----------------------------------------------------------

import sys
n = int(input())

# 각 네트워크 선의 길이에 따른 정답을 담은 배열
# (직관적으로 사용하기위해 0번인덱스 x)
dy = [0]*(n+1)  

# 직관적으로 알 수 있는건 -> 초기화 먼저해주기
dy[1] = 1
dy[2] = 2

# for문을 돌면서 dy배열을 채운다.(1, 2는 채웠으니까 3번부터)
for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]  
    # f(n) = f(n-1) + f(n-2) 이런 공식을 세워야됨
    # 잘라야하는 네트워크 선의 단위가 1,2이므로 
    
answer = dy[n]




# ----------------------------------------------------------
#                   Top - Down 
# ----------------------------------------------------------
import sys
sys.stdin = open("input.txt", 'r')

def DFS(len):
    # 이미 구해진값이 있으면 이것을 이용하는 것 
    # 이 if문 덕분에 재귀가 아니라 DP가 되는 것임
    if dy[len]>0:
        return dy[len]
        
    # 직관적으로 알 수 있는 부분은 DP 종료문이 됨
    if len==1 or len==2:
        return len
        
    else:
        dy[len]=DFS(len-1)+DFS(len-2)  # 값을 저장하는 것이 DP임!
        return dy[len]

if __name__=="__main__":
    n=int(input())
    dy=[0]*(n+1)
    print(DFS(n))

    

