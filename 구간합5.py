import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []
for _ in range(N) :
    arr.append(list(map(int,input().split())))

dp = [[0]*(N+1) for i in range(N+1)]
for i in range(1,N+1) :
    for j in range(1,N+1) :
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]
#dp[i][j]이 arr[i-1][j-1]까지의 합임.
ans = list()
for _ in range(M) :
    x1,y1,x2,y2 = map(int,input().split())
    ans.append(dp[x2][y2] + dp[x1-1][y1-1] - dp[x2][y1-1] - dp[x1-1][y2])
for i in range(len(ans)) :
    print(ans[i])