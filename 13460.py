from collections import deque
import sys
read = sys.stdin.readline

n,m = map(int,read().split())
graph = list()
for _ in range(n) :
    graph.append(list(read().strip('\n')))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

check = [[0]*m for _ in range(n)]
queue1 = deque()
queue2 = deque()

def bfs() :
    while queue1 :
        x,y = queue1.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == '.' and check[nx][ny] == 0:
                while graph[nx][ny] == '.' :
                    check[nx][ny] = check[x][y] + 1
                    nx += dx[i]
                    ny += dy[i]
                if graph[nx][ny] == 'O' :
                    print(check[x][y]+1)
                    return
            if graph[nx][ny] == 'O' :
                print(check[x][y]+1)
                return

for i in range(n) :
    for j in range(m) :
        if check[i][j] == 'R' :
            queue1.append((i,j))
            bfs()
            return
    
