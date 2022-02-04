import sys
read = sys.stdin.readline

n = int(input())
graph = [list(map(int,read().split())) for _ in range(n)]

a,b,c = graph[0][0], graph[0][1], graph[0][2]
x,y,z = graph[0][0], graph[0][1], graph[0][2]

for i in range(1,n) :
    a,b,c = max(a,b)+graph[i][0], max(a,b,c)+graph[i][1], max(b,c)+graph[i][2]
    x,y,z = min(x,y)+graph[i][0], min(x,y,z)+graph[i][1], min(y,z)+graph[i][2]

print(max(a,b,c), min(x,y,z))
