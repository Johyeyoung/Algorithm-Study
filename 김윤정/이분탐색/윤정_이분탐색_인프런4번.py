# 마구간 정하기_결정알고리즘(이분탐색)

magu=[1,2,8,4,9]
n=5
c=3
magu.sort()
lt=1
rt=magu[n-1]


#Count 함수 만들기
def Count(len):
    cnt=1
    ep=magu[0]
    for i in range(1,n):
        if magu[i]-ep>=len:
            cnt+=1
            ep=magu[i]
    return cnt



while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)



