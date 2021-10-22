import sys
read = sys.stdin.readline

ans = 0
n = int(read())

for i in range(1, n+1) :
    if i<=99 :
        ans+=1

    else :
        num = list(map(int,str(i)))
        if num[0]-num[1] == num[1]-num[2] :
            ans+=1
print(ans)
