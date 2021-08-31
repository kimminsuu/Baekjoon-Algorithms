from collections import deque
import sys
read = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs() :
    
    queue.append([0,0,1])
    check = [[[0]*2 for _ in range(m)] for _ in range(n)]
    check[0][0][1] = 1

    while queue :
        x, y, count = queue.popleft()
        if x == n-1 and y == m-1 :
            return check[x][y][count]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m :
                if graph[nx][ny] == 1 and count == 1 :
                    check[nx][ny][0] = check[x][y][1] + 1
                    queue.append((nx,ny,0))
                elif graph[nx][ny] == 0 and check[nx][ny][count] == 0 :
                    check[nx][ny][count] = check[x][y][count] + 1
                    queue.append((nx,ny,count))
    return -1


n,m = map(int,read().split())
graph = list()
for _ in range(n) :
    graph.append(list(read()))
queue = deque()
print(bfs())
