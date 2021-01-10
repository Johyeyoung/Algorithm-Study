# 카드 역배치

a=5
b=10

#swap
#a,b= b,a
#print(a, b)  #10, 5

s=list(range(21))

for i in range((b-a+1)//2):
    s[a+1], s[b-i] = s[b-i], s[a+1]

s.pop(0)
print(s)