import sys
read = sys.stdin.readline
from itertools import combinations

n = int(read())
graph = list()
for _ in range(n) :
    graph.append(list(map(int, read().split())))

mem = [i for i in range(n)]
team = list()
for i in list(combinations(mem, n//2)) :
    team.append(i)

small = 0

for i in range(len(team)//2) :
    t = team[i]
    num1 = 0
    for j in t :
        for k in t :
            num1 += graph[j][k]

    t = team[-i-1]
    num2 = 0
    for j in t :
        for k in t :
            num2 += graph[j][k]

    if i == 0 :
        small = abs(num1-num2)
    else :
        small = min(small, abs(num1-num2))
        
print(small)
