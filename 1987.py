import sys
read = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = list()
alphabets = list()
count = 0

def dfs(x,y) :
    if graph[x][y] in alphabets :
        return
    else :
        count+=1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c :
                dfs(nx,ny)
                list.append(graph[x][y])
                
    
r, c = map(int, read().split())
for _ in range(r) :
    graph.append(list(map(str, read())))

dfs(0,0)
print(count)
