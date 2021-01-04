import sys

#sys.stdin = open("input.txt", "rt")

N = int(input())
lst1 = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

lst = lst1 + lst2
lst.sort()
for i in lst:
    print(i, end=' ')


