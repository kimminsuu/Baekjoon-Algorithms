import sys
input = sys.stdin.readline
s1 = ' '+input().rstrip()
s2 = ' '+input().rstrip()

dp = [['']*len(s2) for i in range(len(s1))]
for i in range(1,len(s1)) :
    for j in range(1,len(s2)) :
        if s1[i] == s2[j] :
            dp[i][j] = dp[i-1][j-1] + s1[i]
        else :
            if len(dp[i-1][j]) >= len(dp[i][j-1]) :
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i][j-1]
result = dp[-1][-1]
print(len(result))

if len(result) != 0:
    print(result)