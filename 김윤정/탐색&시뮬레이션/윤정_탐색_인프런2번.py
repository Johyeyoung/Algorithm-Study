# 2.숫자만 추출

# 문자열에서 숫자 추출하고, 그 수의 약수 개수 출력

a="g0en2Ts8eSoft"

a=list(a)

b=[]

for i in range(len(a)):
    if a[i].isdigit():
        temp=a[i]
        b.append(temp)

if b[0] == '0':
    b.pop(0)

c=''.join(b)
c=int(c)
print(c)

cnt=0

for i in range(1, c+1):
    if c % i == 0:
        cnt+=1

print(cnt)
