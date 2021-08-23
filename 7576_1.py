from collections import deque

m, n = map(int,input().split())
graph = list()
for i in range(n) :
    graph.append(list(map(int, input().split())))

queue = deque()
res = 0

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            queue.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue :
    x,y = queue.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n :
            queue.append((nx,ny))
            graph[nx][ny] = graph[x][y] + 1

for i in graph :
    for j in i :
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)

            
