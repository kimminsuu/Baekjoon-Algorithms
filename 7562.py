import sys
read = sys.stdin.readline
from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(a2,b2) :
    while queue :
        x, y = queue.popleft()
        if x == a2 and y == b2 :
            print(graph[x][y]-1)
            return
        for i in range(8) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0 :
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1



n = int(read())
while n>0 :
    l = int(read())
    graph = [[0] * l for _ in range(l)]
    a1, b1 = map(int, read().split())
    a2, b2 = map(int, read().split())
    graph[a1][b1] = 1
    queue = deque()
    queue.append((a1,b1))
    bfs(a2,b2)
    n-=1
