# 1. 이분검색

#lt와 rt 포인터 변수를 만들고 찾고자 하는 값이
#중간값 보다 큰지 작은지를 판별하여
#포인터를 움직이면서 몇번째에 찾고자하는 값이 있는지 확인
n=8
m=32
a=[23, 87, 65, 12, 57, 32, 99, 81]

a.sort()

lt=0
rt=n-1

while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1