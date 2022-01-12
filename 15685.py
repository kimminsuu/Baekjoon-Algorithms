import sys
read = sys.stdin.readline

graph = [[0]*101 for _ in range(101)]
dx=[0,-1,0,1]
dy=[1,0,-1,0]

n = int(read())
s = list()
for i in range(n) :
    s.append(list(map(int,read().split())))

for _ in range(n) :
    x,y,d,g = map(int,read().split())
    graph[x][y] = 1

    curve = [d]
    for i in range(g) :
        for j in range(len(curve)-1,-1,-1) :
            curve.append((curve[j]+1)%4)

    for i in range(len(curve)) :
        x+=dx[curve[i]]
        y+=dy[curve[i]]
        if 0<x<=101 or 0<y<=101 :
            continue

        graph[x][y] = 1

ans = 0
for i in range(100) :
    for j in range(100) :
        if graph[i][j]==1 and graph[i+1][j] == 1 and graph[i][j+1] == 1and graph[i+1][j+1] == 1 :
            ans+=1

print(ans)
