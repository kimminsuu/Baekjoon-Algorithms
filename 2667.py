from collections import deque

n = int(input())
graph = list()

for i in range(n) :
    graph.append(list(map(int, input())))

aparts = []
check = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 and check[i][j] == 0:
            count = 1
            queue = deque()
            queue.append((i,j))
            check[i][j] = 1
            while queue :
                x,y = queue.popleft()
                for k in range(4) :
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0<=nx<n and 0<=ny<n :
                        if graph[nx][ny] == 0 :
                            continue
                        if graph[nx][ny] == 1 and check[nx][ny] == 0:
                            count+=1
                            queue.append((nx,ny))
                            check[nx][ny] = 1
            aparts.append(count)
aparts.sort()
print(len(aparts))
for i in range(len(aparts)) :
    print(aparts[i])
