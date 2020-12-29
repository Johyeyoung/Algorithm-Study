import sys

def count_DVD(lst, max_time):   # max_time 용량으로 녹음할 수 있는 dvd의 개수 리턴하는 함수
    if max_time == 1:
        return len(lst)
    cnt = 0
    idx = 0
    result = 0
    while idx <= len(lst) - 1:
        cnt += lst[idx]
        if max_time <= cnt:
            result += 1
            cnt = 0
            idx -= 1
        idx += 1
    return result


# sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
lst = list(map(int, input().split()))

lower = 1
upper = sum(lst)
result = 0

while lower <= upper:
    cnt = 0
    mid = (lower + upper) // 2  # 답이 될 수 있는 예비
    #print("mid: ", mid)
    cnt = count_DVD(lst, mid)
    #print("cnt: ", cnt)
    if cnt < M:
        upper = mid - 1
    else:
        result = max(result, mid)
        lower = mid + 1

print(result)



























