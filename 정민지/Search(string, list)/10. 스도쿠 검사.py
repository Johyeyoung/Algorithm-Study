import sys

#sys.stdin = open("input.txt", "rt")
lst = [list(map(int, input().split())) for _ in range(9)]
flg = False

# i(행) = 0~3, 0~3, 0~3 // 3~6, 3~6, 3~6 // 6~9, 6~9, 6~9
# j(열) = 0~3, 3~6, 6~9 // 0~3, 3~6, 6~9 // 0~3, 3~6, 6~9
# => 검사!!
for i in range(3, 10, 3):
    for j in range(3, 10, 3):
        check = set()
        # print("행: ", i-3, " ", i)
        # print("열: ", j-3, " ", j)
        for k in range(i-3, i):
            for h in range(j-3, j):
                if lst[k][h] in check:
                    print("NO")
                    flg = True
                    break
                else:
                    check.add(lst[k][h])
            if flg:
                break

        if flg:
            break
    if flg:
        break
else:
    print("YES")




