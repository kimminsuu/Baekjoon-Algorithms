n = int(input())
s = list(map(int,input().split()))

dp1,dp2 = [1]*n, [1]*n
for i in range(1,n) :
    if s[i]<=s[i-1] :
        dp1[i] = max(dp1[i],dp1[i-1]+1)
    if s[i]>= s[i-1] :
        dp2[i] = max(dp2[i], dp2[i-1]+1)

print(max(max(dp1),max(dp2)))
