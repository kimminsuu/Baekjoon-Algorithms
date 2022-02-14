t = int(input())
for _ in range(t) :
    k = int(input())
    s = list(map(int,input().split()))

    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n-1) :
        dp[i][i+1] = s[i]+s[i+1]
        for j in range(i+2,n) :
            dp[i][j] = dp[i][j-1]+s[j]

    for i in range(2,n) :
        for j in range(n-i) :
            k = i+j
            dp[j][k] += min(
