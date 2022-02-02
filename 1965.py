n = int(input())
s = list(map(int,input().split()))
dp = [1] * (n+1)
for i in range(1,n)  :
    for j in range(i) :
        if s[i] > s[j] :
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
