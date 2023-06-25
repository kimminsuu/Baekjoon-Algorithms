from collections import deque
import copy

di = [0,0,-1,1]
dj = [1,-1,0,0]

def rec(temp, i, j, d, graph2,fillin) :
    if temp > 0:
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            return
        if temp == 5:
            graph2[ni][nj] = temp
            i, j = ni, nj
            rec(temp-1, i, j, d, graph2, True)
        else:
            if d < 2:
                ni1 = i + di[2]
                nj1 = j + dj[2]
                ni2 = i + di[3]
                nj2 = j + dj[3]
                if d == 0:
                    if (i, j, 1) not in byuk:
                        graph2[ni][nj] = temp
                        rec(temp-1,ni,nj,d,graph2, True)
                else :
                    if (ni, nj, 1) not in byuk:
                        graph2[ni][nj] = temp
                        rec(temp-1,ni,nj,d,graph2, True)
                if fillin:
                    if 0 <= ni1 < R and 0 <= nj1 < C:
                        if (i, j, 0) not in byuk:
                            rec(temp,ni1,nj1,d,graph2,False)
                    if 0 <= ni2 < R and 0 <= nj2 < C:
                        if (ni2, nj2, 0) not in byuk:
                            rec(temp, ni2, nj2, d, graph2,False)
            else :
                ni1 = i + di[0]
                nj1 = j + dj[0]
                ni2 = i + di[1]
                nj2 = j + dj[1]
                if d == 2:
                    if (i, j, 0) not in byuk:
                        graph2[ni][nj] = temp
                        rec(temp - 1, ni, nj, d, graph2, True)
                else:
                    if (ni, nj, 0) not in byuk:
                        graph2[ni][nj] = temp
                        rec(temp - 1, ni, nj, d, graph2, True)
                if fillin :
                    if 0 <= ni1 < R and 0 <= nj1 < C:
                        if (i, j, 1) not in byuk:
                            rec(temp, ni1, nj1, d, graph2,False)
                    if 0 <= ni2 < R and 0 <= nj2 < C:
                        if (ni2, nj2, 1) not in byuk:
                            rec(temp, ni2, nj2, d, graph2,False)



def step1(graph) : # 온풍기 바람
    #벽 : c가 1이면 오른쪽, 0이면 위쪽 byuk
    #바람 방향 : 0오 1왼 2위 3아래 q에 온풍기
    for i,j,d in q :
        graph2 = [[0] * C for _ in range(R)]
        temp = 5
        rec(temp, i, j, d, graph2, True)
        for a in range(R) :
            for b in range(C) :
                graph[a][b]+=graph2[a][b]

def step2(graph) : # 온도 조절
    graph2 = copy.deepcopy(graph)
    for i in range(R) :
        for j in range(C) :
            if i < R-1 and (i+1,j,0) not in byuk:
                if graph[i][j] - graph[i + 1][j] > 0 :
                    minus = abs(graph[i][j]-graph[i+1][j]) // 4
                    graph2[i][j] -= minus
                    graph2[i+1][j] += minus
                elif graph[i][j] - graph[i + 1][j] < 0 :
                    minus = abs(graph[i][j]-graph[i+1][j]) // 4
                    graph2[i][j] += minus
                    graph2[i+1][j] -= minus
            if j < C-1 and (i,j,1) not in byuk:
                if graph[i][j] - graph[i][j+1] > 0 :
                    minus = abs(graph[i][j]-graph[i][j+1]) // 4
                    graph2[i][j] -= minus
                    graph2[i][j+1] += minus
                elif graph[i][j] - graph[i][j+1] < 0 :
                    minus = abs(graph[i][j]-graph[i][j+1]) // 4
                    graph2[i][j] += minus
                    graph2[i][j+1] -= minus
    return graph2

def step3() : # 온도 1 이상인 바깥쪽칸 온도 1 감소
    for i in range(R) :
        for j in range(C) :
            if i==0 or i==R-1 or j==0 or j==C-1:
                if graph[i][j] > 0:
                    graph[i][j]-=1

def step4() : # 조사하는 칸이 모두 K이상이면 False
    for (i,j) in q2 :
        if graph[i][j] < K :
            return True
    return False

if __name__ == '__main__' :
    R,C,K = map(int,input().split())

    choco = 0
    graph_temp = list()
    byuk = deque() # 벽 queue 불변
    q = deque() # 온풍기 queue 불변
    q2 = deque() # 조사할 칸 queue 불변

    for _ in range(R) :
        graph_temp.append(list(map(int,input().split())))

    for i in range(R) :
        for j in range(C) :
            if 1 <= graph_temp[i][j] <=4 : #0오 1왼 2위 3아래
                q.append((i,j,graph_temp[i][j]-1))
            elif graph_temp[i][j] == 5 :
                q2.append((i,j))

    W = int(input())
    for _ in range(W) :
        a,b,c = map(int,input().split())
        byuk.append((a-1,b-1,c)) #c가 1이면 오른쪽, 0이면 위쪽

    graph = [[0] * C for _ in range(R)]
    flag = True
    while flag :
        step1(graph)
        graph = step2(graph)
        step3()
        choco +=1
        if choco > 100 :
            choco = 101
            break
        flag = step4()

    print(choco)
