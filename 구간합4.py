import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
ans=[]

dp = [0]*(N+1)
for i in range(1,N+1) :
    dp[i] = dp[i-1] + arr[i-1]
for _ in range(M) :
    i,j = map(int,input().split())
    ans.append(dp[j]-dp[i-1])
for k in range(len(ans)):
    print(ans[k])