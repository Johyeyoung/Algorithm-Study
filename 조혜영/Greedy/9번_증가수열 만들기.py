import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))

lt=0 # 왼쪽 index
rt=n-1 # 오른쪽 index
last=0 # 현재 완성된 수열의 가장 끝 (촤댓값) 


res=""
tmp=[]

# 교차되기 전까지 →, ← 각 방향에서 검사하기
# ------------------------------------
# 이분법 & 인덱스 옮기기!!
# ------------------------------------
while lt<=rt:
    # 양 끝값을 조회하되, 바로 수열로 만드는 것이 아니라
    # 임시 list인 temp에 값을 담아둔다.
    # 항상 last(현재 등록된 수열의 마지막 원소 즉 가장 큰 값)와 비교하여 그보다 큰것이
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    
    # 임시 값으로 담아둔 곳에서 가장 작은것을 선택해 수열(res)로 만든다
    # 이부분이 그리디!!!
    tmp.sort()
    # -----예외처리----------
    if len(tmp)==0:
        break;
    else:
        res=res+tmp[0][1] # 선택된 원소의 방향(R, L)을 기록하고
        last=tmp[0][0]  # 현재 수열에 추가된 원소를 last에 올린다 
        # 선택된 원소의 인덱스를 당겨준다
        if tmp[0][1]=='L':
            lt=lt+1
        else:
            rt=rt-1
    tmp.clear()

print(len(res))
print(res)
