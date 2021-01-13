 
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
