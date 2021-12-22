import sys
read = sys.stdin.readline
from collections import deque
import copy

n,m = map(int,read().split())
graph = list()
for i in range(n) :
    graph.append(list(map(int,read().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
_max = 0

def bfs() :
    global _max
    arr = copy.deepcopy(graph)
    queue = deque()
    res = 0
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 2 :
                queue.append((i,j))

    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny] == 0 :
                    arr[nx][ny] = 2
                    queue.append((nx,ny))
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 0 :
                res+=1
    _max = max(_max,res)
    

def func(count) :
    if count == 3 :
        bfs()
        return
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 0 :
                graph[i][j] = 1
                func(count+1)
                graph[i][j] = 0

func(0)
print(_max)
