from collections import deque
dj = [0,1,-1,0]
di = [1,0,0,-1]

def seek() :
    a,b = shark.popleft()
    q = deque([(a,b)])
    visit = [[0]*N for _ in range(N)]
    visit[a][b] = 1
    size = big[0]
    graph[a][b] = 0
    while q :
        i,j = q.popleft()
        for k in range(4) :
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N and visit[ni][nj] == 0 :
                if graph[ni][nj] < size and graph[ni][nj]!=0:
                    visit[ni][nj] = visit[i][j] + 1
                    q.append((ni,nj))
                    fish.append((ni,nj,visit[ni][nj]-1))
                elif graph[ni][nj] == 0 :
                    visit[ni][nj] = visit[i][j] + 1
                    q.append((ni,nj))
                elif graph[ni][nj] == size :
                    visit[ni][nj] = visit[i][j] + 1
                    q.append((ni,nj))


if __name__ == '__main__':
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
    shark = deque()
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] == 9 :
                shark.append((i,j))
    big = [2,0]
    tot = 0
    fish = []
    while True :
        fish.clear()
        seek()
        if not fish :
            break
        fish.sort(key=lambda x : (x[2],x[0],x[1]))
        a,b,s = fish[0]
        tot += s
        big[1] +=1
        graph[a][b] = 9
        shark.append((a,b))
        if big[1] == big[0] :
            big[0]+=1
            big[1] = 0
    print(tot)


