# 랜선 자르기 _결정 알고리즘(이분탐색)

k=4
n=11
line=[802, 743, 457, 539]

res=0

#Count함수 만들기
def Count(len):
    cnt=0
    for x in line:
        cnt+=(x//len)
    return cnt

#가장 긴 랜선찾기
largest=0
largest=max(line)

#이분검색
lt=1
rt=largest

while lt <=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)