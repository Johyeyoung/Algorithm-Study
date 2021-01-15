def solution(m, n, puddles):
    dy =[[0] * (m+1) for _ in range(n+1)]
    dy[1][1] = 1
    # 2차원배열 초기화 사이드쪽
    for i in range(1, n+1): # 행
        for j in range(1, m+1): # 열
            if [j, i] not in puddles:
                if i == 1 and j == 1: continue # 1, 1 좌표는 이미1로 초기화했던거 건들면 안됨 건들면 0이됨
                if j == 1:
                    dy[i][j] = dy[i-1][j]
                elif i == 1:
                    dy[i][j] = dy[i][j-1]
            else:
                dy[i][j] = 0    
                
    # 2차원 배열 안쪽 채우기
    for i in range(2, n+1): # 행
        for j in range(2, m+1): # 열
            if [j, i] not in puddles: # 연못이 아닌 경우만 경로수 update
                dy[i][j] = dy[i-1][j]+dy[i][j-1]   
            else: # 연못이면 건너뛰는게 아니라 0으로 해줘야 다음 좌표에서 연못부분인걸 확인하고 안더하는 효과생김
                dy[i][j] = 0
    answer = dy[n][m]%1000000007
    
    return answer
