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

    

