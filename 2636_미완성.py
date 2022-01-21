import sys
read = sys.stdin.readline
from collections import deque

n,m = map(int,read().split())
graph = [list(map(int,read().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
flag = False

visit = [[False]*m for _ in range(n)]
count = 0
num2 = 0
while(True) :
    print(graph)
    num = 0
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1:
                num+=1
                flag = True
                for k in range(4) :
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 :
                        visit[i][j] = True

    if not flag :
        print(count)
        print(num2)
        break
    else :
        num2 = num
        count+=1
        flag = False
        for i in range(n) :
            for j in range(m) :
                if visit[i][j] == True :
                    graph[i][j] = 0
                    visit[i][j] = False
            
                    
