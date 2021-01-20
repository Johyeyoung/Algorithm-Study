#-------------------------------------------------------------------------
#                           5번. 공주구하기
#-------------------------------------------------------------------------

import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
q=list(range(1, n+1))
dq=deque(q)
while dq:
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()



#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
	freopen("input.txt", "rt", stdin);
	int n, k, p=0, i, bp=0, cnt=0;
	scanf("%d %d", &n, &k);

  vector<int> prince(n+1); 
  
  // 마지막 왕자 한명 남을때까지 돌기
	while(1){
		p++;
		if(p>n) p=1;
		if(prince[p]==0){ //queue 안에 있는 왕자를 대상으로만 k번째 외치는지 count!
			cnt++; // cnt는 k까지 도달하는지 확인용
			if(cnt==k){ // k번째 왕자가 나오면 해당 왕자를 queue에서 제거(prince[p]=1)하고 
				prince[p]=1;
				cnt=0;
				bp++; // 제외된 왕자 수 up
			}
		}
		if(bp==n-1) break; // 한명 남을때까지 돌기
	}
	for(i=1; i<=n; i++){
		if(prince[i]==0){
			printf("%d\n", i);
			break;
		}
	}
	return 0;
}







#include<stdio.h>
#include<vector>
using namespace std;
int main(){
	freopen("input.txt", "rt", stdin);
	int n, k, pos=0, i, cnt=0; // n: 왕자의 수, k: 외쳐야할 번호
	scanf("%d %d", &n, &k);
	
  vector<int> prince(n+1); //왕자를 집어넣을 Queue 
	while(1){
    // k를 외치는 왕자가 나타나기 전까지 계속 앞에서 선出 후入 
		for(i=1; i<=k; i++){
      // 이건 큐자료형이 아니라 배열이므로 Queue에 있는(prince[pos]==0)대상으로만 k번째 계산하기임 
			while(1){
				pos++;
				if(pos>n) pos=1; // 다시 인덱스를 원점으로 
				if(prince[pos]==0) break; // 아직 제외되지 않고(prince[pos]==0) 큐에 있음 
			}
		}
		prince[pos]=1;  // 공주구하기에서 제외할 왕자는 prince[i]==1
		cnt++; // 탈출하는 왕자 수 ++ 
		if(cnt==n-1) break; // 마지막 한명 남으면 구출하기!
	}

  // 공주를 구하러갈 왕자(prince[i]==0)를 찾아 출력!
	for(i=1; i<=n; i++){
		if(prince[i]==0){
			printf("%d\n", i);
			break;
		}
	}
	return 0;
}







#-------------------------------------------------------------------------
#                           6번. 응급실
#-------------------------------------------------------------------------


import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break







#-------------------------------------------------------------------------
#                           7번. 교육과정설계
#-------------------------------------------------------------------------

import sys
from collections import deque
sys.stdin=open("input.txt", "r")
need=input()
n=int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
