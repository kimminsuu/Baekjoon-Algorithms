import sys
read = sys.stdin.readline

n = int(read())
graph = [list(map(int,read().split())) for _ in range(n)]
visited = [0 for i in range(n)]

def func(num) :
    for i in range(n) :
        if visited[i]==0 and graph[num][i] == 1 :
            visited[i] = 1
            func(i)

for i in range(n) :
    func(i)
    for j in range(n) :
        if visited[j] == 1 :
            print(1, end='')
        else :
            print(0, end='')
    print()
    visited = [0 for i in range(n)]
