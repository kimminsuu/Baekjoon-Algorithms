import sys
read = sys.stdin.readline
from collections import deque

n = int(read())
graph = [list(map(int,read().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
count = 1
ans = sys.maxsize

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j) :
    global count
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    graph[i][j] = count
    
    while queue :
        x,y = queue.popleft()
        for k in range(4) :
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1 and not visited[nx][ny] :
                visited[nx][ny] = True
                graph[nx][ny] = count
                queue.append((nx,ny))

def func(a) :
    global ans
    queue = deque()
    d = [[-1]*n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if graph[i][j] == a :
                queue.append((i,j))
                d[i][j] = 0

    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n :
                if graph[nx][ny] > 0 and graph[nx][ny] != a :
                    ans = min(ans,d[x][y])
                    return
                if arr[nx][ny] == 0 and d[nx][ny] == -1 :
                    d[nx][ny] = d[x][y]+1
                    queue.append((nx,ny))
            
    

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 and not visited[i][j] :
            bfs(i,j)
            count+=1

for i in range(1,count) :
    func(i)

print(ans)
