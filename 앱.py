N,M = map(int,input().split())
A=[0]+list(map(int,input().split()))
C=[0]+list(map(int,input().split()))

dp = [[0]*(sum(C)+1) for _ in range(N+1)]
result = sum(C)
ans = result+1

for i in range(1,N+1) :
    byte = A[i]
    cost = C[i]
    for j in range(result+1) :
        dp[i][j] = dp[i-1][j]
    for j in range(cost,result+1) :
        dp[i][j] = max(dp[i][j],byte + dp[i-1][j-cost])
        if dp[i][j] >= M :
            ans = min(ans,j)

print(ans)