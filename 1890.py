import sys
read = sys.stdin.readline
from collections import deque

n=int(read())
graph = []
for i in range(n) :
    graph.append(list(map(int,read().split())))

dx = [1,0]
dy = [0,1]

def bfs() :
    global ans
    x,y = queue.popleft()
    if x==n-1 and y==n-1 :
        ans+=1
    
    num = graph[x][y]
    for i in range(2) :
        nx = x+dx[i] * num
        ny = y+dy[i] * num
        if 0<=nx<n and 0<=ny<n :
            queue.append((nx,ny))
            bfs()
        

ans = 0
queue = deque()
queue.append((0,0))
bfs()
