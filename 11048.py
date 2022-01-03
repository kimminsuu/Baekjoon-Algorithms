import sys
read = sys.stdin.readline

graph = list()
n,m = map(int,read().split())
for i in range(n) :
    graph.append(list(map(int,read().split())))

ans = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,m+1) :
        ans[i][j] = graph[i-1][j-1] + max(ans[i-1][j],ans[i][j-1],ans[i-1][j-1])

print(ans[n][m])
