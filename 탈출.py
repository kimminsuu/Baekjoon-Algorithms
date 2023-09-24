from collections import deque

def move() :
    i,j = gosum.popleft()
    board[i][j] = 1
    for k in range(4) :
        ni = i+di[k]
        nj = j+dj[k]
        if 0<=ni<R and 0<=nj<C :
            if graph[ni][nj] == 'X'or graph[ni][nj]=='*':
                continue
            if graph[ni][nj] == 'D':
                return True
            if board[ni][nj] == 0:
                flag = False
                for d in range(4):
                    ti = ni+di[d]
                    tj = nj+dj[d]
                    if 0<=ti<R and 0<=tj<C:
                        if graph[ti][tj]=='*':
                            flag = True
                if not flag:
                    board[ni][nj] = board[i][j]+1
                    gosum.append((ni,nj))
    return False


def water() :
    i,j = mul.popleft()
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if 0<=ni<R and 0<=nj<C:
            if graph[ni][nj] == 'X' or graph[ni][nj] == 'D':
                continue
            if graph[ni][nj] =="*":
                continue
            graph[ni][nj] = "*"
            mul.append((ni,nj))

if __name__=="__main__" :
    di=[-1,1,0,0]
    dj=[0,0,-1,1]

    R,C = map(int,input().split())
    graph = []
    for i in range(R) :
        graph.append(list(map(str,input())))

    gosum = deque()
    mul = deque()

    board = [[0]*C for _ in range(R)]

    for i in range(R) :
        for j in range(C) :
            if graph[i][j] =='S':
                gosum.append((i,j))
            if graph[i][j] == '*' :
                mul.append((i,j))
    ff = False
    num = 0
    while True :
        for m in range(len(gosum)):
            ff = move()
            if ff:
                break
        num += 1
        if ff:
            print(num)
            break

        if not gosum:
            print("KAKTUS")
            break

        for m in range(len(mul)):
            water()
