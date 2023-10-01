import copy
from collections import deque

def step1(): # 냄새살포 , smell 만 바꿔줌
    for i in range(N) :
        for j in range(N) :
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if graph[i][j] != 0 :
                smell[i][j] = [graph[i][j],K]

def step2(): #상어 이동 , graph저장까지
    board = [[0]*N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] != 0 :
                shark = graph[i][j]
                direct = direction[shark-1]
                did = False
                for k in prior[shark-1][direct-1] :
                    ni = i + di[k-1]
                    nj = j + dj[k-1]
                    if 0<=ni<N and 0<=nj<N :
                        if smell[ni][nj][1]==0 :
                            direction[shark-1] = k
                            if board[ni][nj] == 0 :
                                board[ni][nj] = shark
                            else :
                                board[ni][nj] = min(shark,board[ni][nj])
                            did=True
                            break
                if not did :
                    for k in prior[shark - 1][direct - 1]:
                        ni = i + di[k - 1]
                        nj = j + dj[k - 1]
                        if 0 <= ni < N and 0 <= nj < N:
                            if shark == smell[ni][nj][0] :
                                direction[shark - 1] = k
                                board[ni][nj] = shark
                                break
    return board


if __name__=='__main__' :
    N,M,K = map(int,input().split())
    graph = []
    for _ in range(N) :
        graph.append(list(map(int,input().split())))
    direction = list(map(int,input().split()))
    prior = []
    for i in range(M): # [[[2,3,1,4],[4,1,2,3]..[3,4,2,1]],[...]]
        temp = []
        for _ in range(4):
            temp.append(list(map(int, input().split())))
        prior.append(temp)

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    smell = [[[0,0]] * N for _ in range(N)] #상어 번호, 초

    ans = 0
    while True :
        ans+=1
        step1()
        graph = copy.deepcopy(step2())
        flag = False
        for i in range(N) :
            for j in range(N) :
                if graph[i][j]>1 :
                    flag = True
        if not flag :
            print(ans)
            break
        if ans >= 1000 :
            print(-1)
            break


