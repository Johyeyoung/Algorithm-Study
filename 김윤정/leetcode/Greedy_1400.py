#LeetCode 1400. Construct K Palindrome Strings

#https://leetcode.com/problems/construct-k-palindrome-strings/

s="annabelle"
k=2


#s안에 알파벳이 각 몇개가 들어있는지 확인
dict={}
for i in s:
    print(i)
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)


#최소갯수를 구한다고 생각하면됨  
#알파벳의 갯수가 홀수인 것을 카운트
cnt=0
for i in dict:
    if dict[i]%2==1:
        cnt+=1

if cnt<=k and len(s)>=k:
    print("False")
else:
    print("True")

