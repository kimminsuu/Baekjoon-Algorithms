import sys
read = sys.stdin.readline
from collections import deque

n,m = map(int,read().split())
graph = list()

for i in range(n) :
    graph.append(list(str(read().strip("\n"))))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    mmax = 0
    while queue :
        a,b = queue.popleft()
        for i in range(4) :
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != "W" and visit[nx][ny] ==0 :
                visit[nx][ny] =1
                graph[nx][ny] = graph[a][b] + 1
                mmax = max(mmax,graph[nx][ny])
                queue.append((nx,ny))

res = 0
for i in range(n) :
    for j in range(m) :
        if graph[i][j] != "W" :
            visit = [[0]*m for _ in range(n)]
            graph[i][j] = 0
            visit[i][j] = 1
            res = max(res,bfs(i,j))
print(res)
