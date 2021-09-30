import sys
read = sys.stdin.readline

n = int(read())
s = list(map(int,read().split()))

dp = [0] * n
for i in range(n) :
    for j in range(i) :
        if s[i] > s[j] and dp[i] < dp[j] :
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))


