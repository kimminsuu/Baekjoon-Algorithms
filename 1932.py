import sys
read = sys.stdin.readline

n = int(read())
graph = list()
for _ in range(n) :
    graph.append(list(map(int,read().split())))

for i in range(1,n) :
    for j in range(len(graph[i])) :
        if j == 0 :
            graph[i][j] = graph[i-1][j] + graph[i][j]
        elif j == len(graph[i]) -1 :
            graph[i][j] = graph[i][j] + graph[i-1][j-1]
        else :
            graph[i][j] = graph[i][j] + max(graph[i-1][j], graph[i-1][j-1])
print(max(graph[n-1]))
