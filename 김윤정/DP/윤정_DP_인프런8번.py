## 알리바바와 40인의 도둑 (Top-Down)

# D(2,2)는 D(2,1)과 D(1,2)로 나눌 수 있고
# D(2,1)은 D(2,0)과 D(1,1)로,
# D(1,2)은 D(1,1)과 D(0,2)로 나눌 수 있다.  => 메모이제이션


import sys
sys.stdin = open("input.txt", "r")

def DFS(x,y):
    if dy[x][y]>0:
        return dy[x][y]
    if x==0 and y==0:
        return arr[0][0]
    else:
        if y==0:
            dy[x][y] = DFS(x-1, y)+arr[x][y]
             
        elif x==0:
            dy[x][y]=DFS(x, y-1)+arr[x][y]
             
        else:
            dy[x][y]=min(DFS(x-1, y)), DFS(x, y-1)+arr[x][y]
            return dy[x][y]


if __name__=="__main__":
    n=int(input())
    arr= [list(map(int, input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    print(DFS(n-1, n-1))


