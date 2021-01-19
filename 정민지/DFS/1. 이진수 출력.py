import sys

#sys.stdin = open("input.txt", "rt")
n = int(input())
s = ""
result = []

# 강의 풀이
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x%2, end='')

# 내 풀이
def toBin(x):
    if 1 < x:
        result.insert(0, x % 2)     # 이 부분을 함수 호출 후로 바꾸면 insert 0 안해도 됨
        toBin(x // 2)
    else:
        result.insert(0, x)
    return result

result = toBin(n)

for i in result:
    s += str(i)
print(int(s))














