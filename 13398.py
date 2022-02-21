n = int(input())
s = list(map(int,input().split()))
dp = [[0]*n for _ in range(2)]

dp[0][0] = s[0]
dp[1][0] = s[0]

for i in range(1,n) :
    dp[0][i] = max(dp[1][i-1],dp[0][i-1]+s[i])
    dp[1][i] = max(dp[1][i-1]+s[i],s[i])

num = float('-inf')
for i in range(2) :
    for j in range(n) :
        if num < dp[i][j]:
            num = dp[i][j]

print(num)
