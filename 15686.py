import sys
read = sys.stdin.readline
from itertools import combinations

n,m = map(int,read().split())
graph = []
for i in range(n) :
    graph.append(list(map(int,read().split())))

home = []
chicken = []
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            home.append((i,j))
        elif graph[i][j] == 2 :
            chicken.append((i,j))

chick = list(combinations(chicken,m))
res = [0]*len(chick)

for i in home :
    for j in range(len(chick)) :
        ans = 101
        for k in chick[j] :
            a = abs(i[0]-k[0])+abs(i[1]-k[1])
            ans = min(ans,a)
        res[j]+=ans
print(min(res))
