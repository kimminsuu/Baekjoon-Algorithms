n = int(input())
dp = [0]*36
dp[0],dp[1],dp[2] = 1,1,2
for i in range(3,n+1) :
    t = 0
    if i%2 :
        for j in range(i//2) :
            t+= 2*dp[j]*dp[i-j-1]
        dp[i] = t+dp[i//2]**2
    else :
        for j in range(i//2) :
            t+= 2*dp[j]*dp[i-j-1]
        dp[i] = t

print(dp[n])
    
