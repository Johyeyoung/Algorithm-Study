 
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
#                                               TOP - DOWN
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

def count(line, idx): # 이 함수의 목적은 return dy[line][idx]임 
    if dy[line][idx] > 0:
        return dy[line][idx] # 이 함수의 목적은 return dy[line][idx]임 
    
    if line == 0 and idx == 0:
        return tri[0][0] # 이 함수의 목적은 return dy[line][idx]임 
    else:
        # 가지고 있는 방향 중에 가장 큰 값을 선택하는 점화식도출 (예외: 한 방향만 있는 경우는  )
        if idx == 0:
            dy[line][idx] = count(line - 1, idx) + tri[line][idx]
        elif idx == len(tri[line]) - 1:
            dy[line][idx] = count(line - 1, idx - 1) + tri[line][idx]
        else:
            dy[line][idx] = max(count(line-1, idx), count(line-1, idx-1)) + tri[line][idx]

        return dy[line][idx] # 이 함수의 목적은 return dy[line][idx]임 


def solution(triangle):
    answer = 0
    global tri, dy
    tri = triangle
    dy = [[0]* len(triangle) for _ in range(len(triangle))]
    max = 0
    for i in range(len(triangle)):
        x = count(len(triangle)-1, i)
        if max < x:
            max = x
    answer = max
    return answer
