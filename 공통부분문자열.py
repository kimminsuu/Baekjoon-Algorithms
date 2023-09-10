import sys
input = sys.stdin.readline
s1 = '0'+input().rstrip()
s2 = '0'+input().rstrip()

ans = 0 #LCS
l1 = len(s1)
l2 = len(s2)
dp = [[0]*(l2) for _ in range(l1)]
for i in range(1,l1) :
    for j in range(1,l2) :
        if s1[i] == s2[j] :
            dp[i][j] = dp[i-1][j-1] + 1
print(max(map(max,dp)))

'''#해싱
hash = {}
ans = 0
for i in range(len(s1)):
    for j in range(1,len(s1)-i+1) :
        tmp = s1[i:i+j]
        if tmp not in hash :
            hash[tmp] = 1

for i in range(len(s1)):
    for j in range(1,len(s1)-i+1) :
        tmp = s2[i:i+j]
        if tmp in hash :
            ans = max(ans,len(tmp))
print(ans)
'''