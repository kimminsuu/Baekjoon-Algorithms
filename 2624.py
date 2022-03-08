t=int(input())
k=int(input())
l=[[0,0]]

for i in range(k):
    l.append(list(map(int,input().split())))
l.sort()

dp=[[0 for j in range(t+1)] for i in range(k+1)]
for i in range(k+1):
    dp[i][0]=1

for i in range(1,k+1):
    for num in range(l[i][1]+1):
        for j in range(t+1):
            temp=j+num*l[i][0]
            if temp==0:
                continue
            if temp<t+1:
                dp[i][temp]+=dp[i-1][j]
            else:
                break

print(dp[k][t])
