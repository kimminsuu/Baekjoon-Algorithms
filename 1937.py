import sys
sys.setrecursionlimit(10**6)

def dfs(x,y) :
    if check[x][y] < 0:
        check[x][y] = 0
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and forest[x][y] < forest[nx][ny] :
                check[x][y] = max(check[x][y], dfs(nx,ny))
        check[x][y]+=1
    return check[x][y]


n = int(input())
forest = list()
for _ in range(n) :
    forest.append(list(map(int,input().split())))

check = [[-1]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

res = 0
for i in range(n) :
    for j in range(n) :
        res = max(res, dfs(i,j))
print(res)
