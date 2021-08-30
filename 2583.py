from collections import deque
import sys
read = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(count,x,y) :
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1

    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx,ny))
                count+=1
    return count

m,n,k = map(int, read().split())

graph = [[0] * n for _ in range(m)]
nums = list()
for _ in range(k) :
    a1,b1,a2,b2 = map(int,read().split())
    for i in range(a1,a2) :
        for j in range(b1,b2) :
            graph[j][i] = 1

for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 0 :
            count = 1
            count = bfs(count,i,j)
            nums.append(count)

print(len(nums))
nums.sort()
for i in range(len(nums)) :
    print(nums[i], end=' ')
