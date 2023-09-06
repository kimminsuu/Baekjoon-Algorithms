arr = list(map(str,input()))

ans = 0
stick = 0
for i in range(len(arr)) :
    if arr[i] == '(' :
        stick+=1
    else :
        if arr[i-1] =='(' :
            stick-=1
            ans += stick
        else :
            stick-=1
            ans+=1
print(ans)
