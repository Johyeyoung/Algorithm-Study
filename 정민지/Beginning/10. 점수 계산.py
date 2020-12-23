import sys

# sys.stdin = open("input.txt", "rt")
N = int(input())
lst = list(map(int, input().split()))
score = 0
pre = 0

if lst[0] == 1:
    pre = 1
    score += 1

for i in range(1, len(lst)):
    if lst[i] == 1:
        pre += 1
        if 1 <= pre:
            score += pre
    else:
        pre = 0

print(score)


