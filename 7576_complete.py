from collections import deque

m, n = map(int,input().split())
graph = list()
for i in range(n) :
    graph.append(list(map(int, input().split())))

queue = deque()
count = 0
res = 0

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            queue.append((i,j))
            
queue.append((-1,-1))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue :
    x,y = queue.popleft()
    if x == -1 and y == -1 :
        count += 1
        if queue :
            queue.append((-1,-1))
        continue
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m :
            if graph[nx][ny] == -1 :
                continue
            if graph[nx][ny] == 0 :
                graph[nx][ny] = 1
                queue.append((nx,ny))

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0:
            res = -1
if res == -1 :
    print(res)
else :
    print(count-1)
            

