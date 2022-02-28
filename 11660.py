import sys
read = sys.stdin.readline
n,m = map(int,read().split())
dp = [[0] *(n+1)] for _ in range(n+1)]
s = [list(map(int,read().split())) for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        d[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - do[i][j] + s[i][j]

for i in range(m) :
    a,b,c,d = map(int,read().split())
    print(dp[c][d] - (dp[a-1][d]+dp[c][b-1]-dp[a-1][b-1]))
