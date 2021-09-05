import sys
from collections import deque
read = sys.stdin.readline

m, n, h = map(int,read().split())
graph = list()
queue = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

for i in range(h) :
    temp = list()
    for j in range(n) :
        temp.append(list(map(int,read().split())))
        for k in range(m) :
            if temp[j][k] == 1 :
                queue.append((i,j,k))
    graph.append(temp)

while queue :
    x,y,z = queue.popleft()
    for i in range(6) :
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz] == 0 :
            queue.append((nx,ny,nz))
            graph[nx][ny][nz] = graph[x][y][z]+1

count = 0
for i in graph :
    for j in i :
        for k in j :
            if k == 0 :
                print(-1)
                exit(0)
        count = max(count,max(j))
print(count-1)
