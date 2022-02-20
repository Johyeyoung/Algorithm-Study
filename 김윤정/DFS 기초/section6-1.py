##재귀함수를 이용한 이진수 출력
#10진수 N이 들어오면 2진수로 변환하여 출력



def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end=" ")

if __name__ == "__main__":
    n=int(input())
    DFS(n)