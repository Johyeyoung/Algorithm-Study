#수열 추측하기(순열, 파스칼 응용)

if __name__ == '__main__':
    n,f =map(int, input().split())
    p=[0]*n
    b=[1]*n  #이항개수의 맨끝은 다 1이기때문에 1로 초기화
    ch=[0]*(n+1)
