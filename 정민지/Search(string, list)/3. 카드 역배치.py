import sys

#sys.stdin = open("input.txt", "rt")

cards = [i for i in range(21)]

for i in range(10):
    ai, bi = map(int, input().split())
    cards[ai:bi+1] = reversed(cards[ai:bi+1])

for i in range(1, 21):
    print(cards[i], end=' ')


