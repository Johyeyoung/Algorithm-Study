import sys


def palindrome(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst)-i-1]:

            return False
    return True

#sys.stdin = open("input.txt", "rt")
cnt = 0
lst = [list(map(int, input().split())) for _ in range(7)]

# 가로 탐색
for i in range(7):
    for j in range(7):
        for k in range(j+1, 7):
            if k-j+1 == 5 and palindrome(lst[i][j:k+1]):
                cnt += 1

# 세로 탐색 -> 포기
for i in range(7):
    for j in range(3):
        for k in range(j, (j+5)//2-1):
            print(k, " ", i)

            if lst[k][i] != lst[4-k][i]:
                break
        else:
            cnt += 1

# 강의 풀이
for i in range(3):  # 5자리만 확인하면 되므로 시작이 0, 1, 2 인 행, 열 만 탐색
    for j in range(7):
        tmp = lst[j][i:i+5]     # 행 탐색
        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(2):      # 열 탐색(처음 두 개의 값과 5자리부터 거꾸로 두 개의 값 비교)
            if lst[i+k][j] != lst[i+5-k-1][j]:
                break
        else:
            cnt += 1


print(cnt)




