#이진트리순회

#DFS 문제를 풀때 DFS 함수가 종료되는 시점을 찾아서 If 조건문으로 탈출 할 수 있도록 설정

#print를 맨 뒤에 찍으면 후위순회 -> 병합정렬이 대표적 사례
#print를 맨 앞에 찍으면 전위순회 DFS는 전위순회가 전반적으로 쓰임
def DFS(v):
    if v > 7:
        return
    else:
        print(v)
        DFS(v*2)
        DFS(v*2+1)
        

if __name__ == "__main__":
    DFS(1)