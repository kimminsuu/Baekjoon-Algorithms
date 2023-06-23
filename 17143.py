from collections import deque
import copy

dx = [0,0,1,-1]
dy = [-1,1,0,0]

fisher = -1
total = 0

def catch(graph,q) :
    global fisher, total
    fisher+=1
    for i in range(R) :
        if graph[i][fisher] != 0 :
            total += graph[i][fisher][2]
            graph[i][fisher] = 0
            target = (i, fisher)
            q = deque(filter(lambda x: x[0:2] != target, q)) #이 방법 숙지하기
            break
    return q
def shark(graph,q) :
    for _ in range(len(q)) :
        graph2 = [[0]*C for _ in range(R)]
        i,j,s,d,z = q.popleft() #s = 속, d = 0,1,2,3 , z=크기
        graph2[i][j] = (s, d, z)
        for _ in range(s) :
            ni = i + dy[d]
            nj = j + dx[d]
            if 0<=ni<R and 0<=nj<C :
                graph2[ni][nj] = graph2[i][j]
                graph2[i][j] = 0
                i,j = ni,nj
            else :
                if d % 2 == 0 : # d방향 바꾸고
                    d+=1
                else :
                    d-=1
                ni = i + dy[d]
                nj = j + dx[d]
                graph2[ni][nj] = graph2[i][j]
                graph2[i][j] = 0
                i,j = ni,nj

        q.append((i,j,s,d,z))

    graph2 = [[0] * C for _ in range(R)]
    for _ in range(len(q)):
        i, j, s, d, z = q.popleft()
        if graph2[i][j] == 0:
            graph2[i][j] = (s, d, z)
            q.append((i, j, s, d, z))
        else :
            if graph2[i][j][2] > z :
                continue
            else :
                graph2[i][j] = (s, d, z)
                q.append((i, j, s, d, z))
    temp = copy.deepcopy(graph2)
    return temp, q

if __name__ == '__main__' :
    R,C,M = map(int,input().split())
    graph = [[0]*C for _ in range(R)]
    q = deque()
    for _ in range(M) :
        r,c,s,d,z = map(int,input().split())
        graph[r-1][c-1] = (s,d-1,z) #방향은 0위 1아래 2오른 3왼
        q.append((r-1, c-1, *graph[r-1][c-1][0:3]))

    for _ in range(C) :
        q = catch(graph,q)
        graph, q = shark(graph,q)
    print(total)