import sys
sys.setrecursionlimit(10**6)

read = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(height,x,y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and not check[nx][ny] and graph[nx][ny]>height:
            check[nx][ny] = 1
            dfs(height,nx,ny)


n = int(read())
graph = list()
res = 1

for _ in range(n) :
    graph.append(list(map(int,read().split())))

for h in range(max(map(max,graph))) :
    check = [[0]*n for _ in range(n)]
    safe = 0
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] > h and not check[i][j] :
                safe+=1
                check[i][j] = 1
                dfs(h,i,j)
    res = max(res, safe)
print(res)
