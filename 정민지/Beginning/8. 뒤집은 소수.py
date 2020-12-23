import sys

def reverse(x):
    return int(str(x)[::-1])

def isPrime(x):
    if x == 1:
        return False

    result = True
    for i in range(2, int(x/2 +1)):
        if x % i == 0:
            result = False
            break
    return result

# sys.stdin = open("input.txt", "rt")
N = int(input())
num_lst = list(map(int, input().split()))
result_lst = [isPrime(reverse(i)) for i in num_lst]
for i in range(len(result_lst)):
    if result_lst[i]:
        print(reverse(num_lst[i]), end=' ')
