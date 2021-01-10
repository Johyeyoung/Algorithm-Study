

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                     9번. 봉우리 (2차원 배열)
#            (지점 설정) a[i+dx[k]][j+dy[k] : (i, j)번째 지점의 상하좌우 탐색
#…………………………………………………………………………………………………………………………………………………………………………………………

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
# ----------------2차원 배열 입력: n*n------------------
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
        # (i, j)번째 지점의 상하좌우 탐색
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):  
            cnt+=1
print(cnt)






#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                      10번. 스도쿠 (행탐색 + 열탐색 + 그룹탐색)
#
#            (지점 설정) a[i*3+k][j*3+s] : (i,j)번째 그룹의 3*3 격자판 탐색 
#…………………………………………………………………………………………………………………………………………………………………………………………

def check(a):
    # _________행/열 탐색__________
    for i in range(9):
        # visited 같은 개념의 배열을 생성해서 해당 열이나 행에 값이 존재하면 1
        ch1=[0]*10  
        ch2=[0]*10
        
        for j in range(9):  
            ch1[a[i][j]]=1  # → 방향으로 check
            ch2[a[j][i]]=1  # ↓ 방향으로 check
        # 모든 0~9까지 다 채워져있으면 다 1이니까 합이 10이됨 10이 아니라는건 중복이 발생한 것    
        if sum(ch1)!=9 or sum(ch2)!=9: 
            return False # 중복 발견 탈락!
    
    # _________3x3 그룹 탐색__________
    # 총 격자판에 있는 9개의 그룹, 그 하나하나의 그룹을 지칭
    for i in range(3):  #(0, 1, 2)
        for j in range(3): #(0, 1, 2)
            ch3=[0]*10
            # 하나의 그룹에서 0~9까지 있는지 check
            for k in range(3): 
                for s in range(3):
                    # (i, j)번째 그룹의 격자 탐색 
                    ch3[a[i*3+k][j*3+s]]=1  # 3*를 해주는 이유 그룹의 단위가 3개씩이니까 3행의 0번쨰~이런식
            if sum(ch3)!=9:
                return False # 중복 발견 탈락!
    return True

 # ----------------2차원 배열 입력: 9*9------------------
a=[list(map(int, input().split())) for _ in range(9)] 
if check(a):
    print("YES")
else:
    print("NO")
    
    
    
    
    
    
    
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#                   11번. 격자판 회문수 (그룹탐색)
#
#        (지점 설정) board[j][i:i+5] : (j,i)번째 그룹의 5글자 탐색 (j행의 5개씩 슬라이스)
#        (지점 설정) board[i+k][j]!=board[i+5-k-1][j] : j열은 유지하고 세로로 i~i+5번째행 check
#…………………………………………………………………………………………………………………………………………………………………………………………    
    
# ----------------2차원 배열 입력: 7*7------------------
board=[list(map(int, input().split())) for _ in range(7)]  
cnt=0

# 숨겨진 그룹을 찾아야됨 
for i in range(3): # 길이가 5인 회문만 찾으니까 7개중에는 3개의 그룹이 나옴 
    for j in range(7):
        tmp=board[j][i:i+5] # j행에서 5개씩 3그룹 슬라이스
        if tmp==tmp[::-1]: # tmp[::-1] 역순으로 뒤집어버리는것 abc ->cba
            cnt+=1
            
        # 세로줄도 확인해야됨 (j열 확인!)
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break;
        else:
            cnt+=1
print(cnt)




<회문의 길이가 가변적일 때 코드>
# ----------------2차원 배열 입력: 7*7------------------
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
len=5
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+len]
        if tmp==tmp[::-1]:
            cnt+=1
        #tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
        for k in range(len//2):
            if board[i+k][j]!=board[len-k+i-1][j]:
                break;
        else:
            cnt+=1
        
print(cnt)
