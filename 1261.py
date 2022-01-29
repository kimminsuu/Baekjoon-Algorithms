import sys
read = sys.stdin.readline
from collections import deque

n,m = map(int,read().split())
graph = [list(map(int,read().strip("\n"))) for _ in range(m)]

visited = [[-1]*n for _ in range(m)]
queue = deque()
queue.append((0,0))
visited[0][0] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue :
    x,y = queue.popleft()
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n :
            if visited[nx][ny] == -1 :
                if graph[nx][ny] == 0 :
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y]
                elif graph[nx][ny] == 1 :
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

print(visited[m-1][n-1])
