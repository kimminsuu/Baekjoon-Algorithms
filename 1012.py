from collections import deque
t = int(input())

def bfs(x, y) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m :
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0

for i in range(t) :
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k) :
        a,b = map(int,input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 :
                bfs(i,j)
                cnt += 1
    print(cnt)
