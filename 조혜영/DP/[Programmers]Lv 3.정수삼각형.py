 
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
#                                               TOP - DOWN
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

def count(line, idx):
    if dy[line][idx] > 0:
        return dy[line][idx]
    
    if line == 0 and idx == 0:
        return dy[line][idx]
    else:
        if idx == 0:
            dy[line][idx] = count(line - 1, idx) + tri[line][idx]
        elif idx == len(tri[line]) - 1:
            dy[line][idx] = count(line - 1, idx - 1) + tri[line][idx]
        else:
            dy[line][idx] = max(count(line-1, idx), count(line-1, idx-1)) + tri[line][idx]

        return dy[line][idx]


def solution(triangle):
    answer = 0
    global tri, dy
    tri = triangle
    dy = [[0]* len(triangle) for _ in range(len(triangle))]
    dy[0][0] = triangle[0][0]
    max = 0
    for i in range(len(triangle)):
        x = count(len(triangle)-1, i)
        if max < x:
            max = x
    answer = max
    return answer
