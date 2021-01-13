import sys
from collections import Counter

#sys.stdin = open("input.txt", "rt")
word1 = input()
word2 = input()

dic1 = Counter(word1)
dic2 = Counter(word2)

if dic1 == dic2:
    print("YES")
else:
    print("NO")
