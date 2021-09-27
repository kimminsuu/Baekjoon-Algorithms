import sys
from collections import deque
read = sys.stdin.readline

n,l,r = map(int, read().split())
graph = list()
for _ in range(n) :
    graph.append(list(map(int,read().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,temp) :
    queue = deque()
    queue.append((i,j))
    temp.append([i,j])
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0 :
                if l <= abs(graph[nx][ny]-graph[x][y]) <=r :
                    visit[nx][ny] = 1
                    queue.append((nx,ny))
                    temp.append([nx,ny])


day = 0
while True :
    visit = [[0]*n for _ in range(n)]
    flag = False
    temp = list()
    for i in range(n) :
        for j in range(n) :
            if visit[i][j] == 0 :
                visit[i][j] = 1
                bfs(i,j,temp)
                print(temp)
                if len(temp) > 1 :
                    flag = True
                    avg = sum(graph[x][y] for x,y in temp) // len(temp)
                    for x,y in temp :
                        graph[x][y] = avg
                    print(graph)
    if not flag :
        break
    day += 1
    print(day)
print(day)




                    
