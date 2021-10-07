import sys
read = sys.stdin.readline

n = int(read())
graph = [0]
for _ in range(n) :
    graph.append(int(read()))

dp = [0]
dp.append(graph[1])

if n > 1 :
    dp.append(graph[1] + graph[2])

for i in range(3, n+1) :
    dp.append(max(dp[i-1], dp[i-2]+graph[i], dp[i-3] + graph[i-1]+graph[i]))
print(dp[n])
