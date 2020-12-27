import sys
sys.stdin=open("input.txt", "r")
n=int(input()) #들어올 원소의 개수
a=list(map(int, input().split())) # a 배열: 각각의 해당 index지점 앞에 index보다 큰 원소의 개수를 담음

# ------정답을 채울 배열---------
seq=[0]*n

# a list를 다 확인한다.
for i in range(n):
    
    # 
    for j in range(n):
        # a[i]는 앞에 i보다 큰 원소의 개수
        # ex) 3 5 2 4 1: a[1]은 5의 의미-> 어떤 배열에서 2(index)앞에 2보다 큰원소가 5개있다   
        # "a[i]==0" 앞에 i보다 큰 원소가 없는 와중에
        # 빈자리("seq == 0") 발견하면 바로 착석
        if(a[i]==0 and seq[j]==0):
            seq[j]=i+1  # 해당 원소를 채운다.
            break
        # 빈자리는 있는데 아직 앞에 큰원소가 있다면 뒤로 물러난다 대신 물러난 만큼  a[i]-=1
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x, end=' ') 
    
    
    '''
    이 문제도 오름차순에 근거하여 그리디 접근이 가능한 것
    오름차순으로 역순열이 각 인덱스에 해당하는 앞의 큰원소의 수를 나눴기에 
    seq의 빈자리에 착석하는 방식을 적용할떄도 →이렇게 한칸씩 뒤로 가며  자기 자리 착석하는 알고리즘이 가능
    '''
