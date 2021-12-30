import sys
read = sys.stdin.readline

graph = list()
zero = list()

for i in range(9) :
    graph.append(list(map(int,read().split())))

for i in range(9) :
    for j in range(9) :
        if graph[i][j] == 0 :
            zero.append((i,j))

def Row(x,n) :
    for i in range(9) :
        if n==graph[x][i] :
            return 0
    return 1

def Col(y,n) :
    for i in range(9) :
        if n==graph[i][y] :
            return 0
    return 1

def Nemo(x,y,n) :
    xx = x//3 * 3
    yy = y//3 * 3
    for i in range(3) :
        for j in range(3) :
            if n == graph[xx+i][yy+i] :
                return 0
    return 1

def dfs(num) :
    if num == len(zero) :
        for i in range(9) :
            print(*graph[i])
        exit(0)

    for i in range(1,10) :
        x = zero[num][0]
        y = zero[num][1]

        if Row(x,i) and Col(y,i) and Nemo(x,y,i) :
            graph[x][y] = i
            dfs(num+1)
            graph[x][y] = 0

dfs(0)
