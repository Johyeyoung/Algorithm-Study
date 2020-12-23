import sys


def digit_sum(x):
    str_x = str(x)
    str_x_lst = list(str_x)
    str_x_lst = [int(num) for num in str_x_lst]
    result = sum(str_x_lst)

    return result


# sys.stdin = open("input.txt", "rt")
N = int(input())
nums = list(map(int, input().split()))
sums = [digit_sum(i) for i in nums]
print(nums[sums.index(max(sums))])
