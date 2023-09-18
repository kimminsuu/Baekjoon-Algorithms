import copy

def dfs(si,sj,score,graph) :
    global tot
    score += graph[si][sj][0]
    graph[si][sj][0] = 0
    tot = max(tot,score)
    for k in range(1,17) :
        i,j=-1,-1
        flag = False
        for ii in range(4) :
            for jj in range(4) :
                if graph[ii][jj][0] == k:
                    i,j=ii,jj
                    flag = True
                    break
        if not flag :
            continue
        d = graph[i][j][1]
        for rd in range(8) :
            num = (rd+d) % 8
            ni = i+di[num]
            nj = j+dj[num]
            if 0<= ni < 4 and 0<=nj<4 and not (si==ni and sj==nj) :
                graph[i][j][1] = num
                graph[ni][nj],graph[i][j] = graph[i][j],graph[ni][nj]

                break
    d = graph[si][sj][1]
    ni = si
    nj = sj
    while True :
        ni+=di[d]
        nj+= dj[d]
        if 0<=ni<4 and 0<=nj<4:
            if graph[ni][nj][0]>0:
                dfs(ni,nj,score,copy.deepcopy(graph))
            else :
                continue
        else :
            break

if __name__ == '__main__' :
    graph = [[] for _ in range(4)]

    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, -1, -1, -1, 0, 1, 1, 1]

    for i in range(4):
        data = list(map(int, input().split()))
        for j in range(4):
            # 물고기 번호, 방향
            graph[i].append([data[2 * j], data[2 * j + 1] - 1])

    tot = 0
    dfs(0,0,0,copy.deepcopy(graph))
    print(tot)