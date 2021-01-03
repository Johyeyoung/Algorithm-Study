# 뮤직비디오_결정알고리즘(이분탐색)

n=9
m=3
songs=[1,2,3,4,5,6,7,8,9]

#Count함수 만들기
def Count(capa):

    cnt=1
    sum=0
    for x in songs:
        if sum+x>capa:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt


lt=1
rt=sum(songs)
maxx=max(songs)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1

    else:
        lt=mid+1
print(res)