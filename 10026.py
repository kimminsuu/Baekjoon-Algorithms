import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
graph = list()
num = [[0] * n for _ in range(n)]

for _ in range(n) :
    graph.append(list(map(str,read())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

def bfs(x,y) :
    num[x][y] = count
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and num[nx][ny]==0:
                num[nx][ny] = num[x][y]
                queue.append((nx,ny))
            
count = 0
for i in range(n) :
    for j in range(n) :
        if num[i][j] == 0:
            count+=1
            queue.append((i,j))
            bfs(i,j)
print(count)

num = [[0] * n for _ in range(n)]
count = 0
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 'G' :
            graph[i][j] = 'R'

for i in range(n) :
    for j in range(n) :
        if num[i][j] == 0:
            count+=1
            queue.append((i,j))
            bfs(i,j)
print(count)
