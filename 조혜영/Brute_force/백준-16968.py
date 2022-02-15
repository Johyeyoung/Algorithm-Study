from string import ascii_lowercase
 
tmpl = input() 

def dfs(n, s):
    global tmpl, cnt 
    if n == len(tmpl)-1:
        cnt += 1
        
    else:
        newNum = list(range(10))
        newStr = list(ascii_lowercase)
        if tmpl[n] == 'd': newNum.remove(s)
        elif tmpl[n] == 'c': newStr.remove(s)

        if tmpl[n+1] == 'd':
            for i in newNum:
                dfs(n+1, i)
            
        elif tmpl[n+1] == 'c':
            for i in newStr:
                dfs(n+1, i)
    

level = len(tmpl)
cnt = 0
if tmpl[0] == 'd':
    for i in range(10):
        dfs(0, i)
elif tmpl[0] == 'c':
    for i in list(ascii_lowercase):
        dfs(0, i)
        
print(cnt)
