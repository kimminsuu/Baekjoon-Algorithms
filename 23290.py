import copy
from collections import deque

di = [0,-1,-1,-1,0,1,1,1]
dj = [-1,-1,0,1,1,1,0,-1]

di2 = [-1,0,1,0]
dj2 = [0,-1,0,1]

def step1() : # 복제마법 시전
    for (i,j,d) in fish :
        fish2.append((i,j,d))

def step2() : # 물고기 이동 (상어, 냄새, 범위 밖 이동 불가)
    for _ in range(len(fish)) :
        i,j,d = fish.popleft()
        num = 0
        for k in range(8) :
            num = k
            ni = i+di[d]
            nj = j+dj[d]
            if  0<=ni<4 and 0<=nj<4 :
                if graph[ni][nj] == 0:
                    fish.append((ni,nj,d))
                    break
                else :
                    d = (d+7) % 8
                    continue
            else:
                d = (d + 7) % 8
                continue
        if num == 7 :
            fish.append((i,j,d))


def step3() : # 상어가 연속 3칸 이동 (상1 좌2 하3 우4)
    global maxfish
    graph2 = [[0]*4 for _ in range(4)]
    for _ in range(len(fish)) :
        i, j, d = fish.popleft()
        graph2[i][j] += 1
        fish.append((i,j,d))

    i,j = shark.popleft()
    erase = list()
    dfs(graph2,i,j,-3,False,3,0,erase)
    for (a,b) in toerase :
        if graph2[a][b] !=0 :
            graph[a][b] = -3
            for _ in range(len(fish)):
                ii,jj,dd = fish.popleft()
                if ii==a and jj==b :
                    continue
                else :
                    fish.append((ii,jj,dd))
    shark.append(toerase[3])

def dfs(graph2,i,j,prev_way, plus_flag, count, fishnum, erase) :
    global maxfish
    global toerase
    erase2 = copy.deepcopy(erase)
    if count < 0:
        if fishnum >= maxfish :
            maxfish = fishnum
            toerase = copy.deepcopy(erase)
        return
    if 0<=i<4 and 0<=j<4 :
        erase2.append((i, j))
        if plus_flag :
            fishnum+=graph2[i][j]
        for k in range(3,-1,-1) :
            ni = i + di2[k]
            nj = j + dj2[k]
            if abs(k-prev_way) ==2 :
                dfs(graph2,ni,nj,k,False,count-1,fishnum,erase2)
            else :
                dfs(graph2, ni, nj, k, True, count - 1, fishnum,erase2)
    else :
        return


def step4() : # 냄새 사라짐
    for i in range(4) :
        for j in range(4) :
            if graph[i][j] <=-4 :
                graph[i][j] +=4
            if graph[i][j] <0 :
                graph[i][j] += 1
            if (i,j) in shark :
                graph[i][j] -= 4


if __name__ == '__main__' :
    M,S = map(int,input().split())
    fish = deque()
    fish2 = deque()
    shark = deque()
    graph = [[0] * 4 for _ in range(4)]

    for _ in range(M) :
        i,j,d = map(int,input().split())
        fish.append((i-1,j-1,d-1))
    for _ in range(1) :
        i, j = map(int, input().split())
        shark.append((i-1,j-1))
        graph[i-1][j-1] = -4

    for _ in range(S) :
        step1()
        step2()
        maxfish = -1
        toerase = list()
        step3()
        step4()
        while fish2 :
            i,j,d = fish2.popleft()
            fish.append((i,j,d))

    print(len(fish))