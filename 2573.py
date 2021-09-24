import sys
from collections import deque
import copy
read = sys.stdin.readline

n,m = map(int, read().split())
graph = list()
for _ in range(n) :
    graph.append(list(map(int, read().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def func1(x, y, after) :
    after[x][y] = graph[x][y]
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 :
            if(after[x][y] == 0) : break
            after[x][y] -= 1

def bfs(after) :
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and after[nx][ny] != 0 :
                queue.append((nx,ny))
                after[nx][ny] = 0
    
    
count = 0
while True :
    count+=1
    after = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] :
                func1(i,j,after)
            
    graph = copy.deepcopy(after)
    queue = deque()
    for i in range(n) :
        for j in range(m) :
            if after[i][j] > 0 :
                queue.append((i,j))
                ans+=1
                bfs(after)
    if ans >= 2 :
        print(count)
        break
    elif ans == 0 :
        print(0)
        break



