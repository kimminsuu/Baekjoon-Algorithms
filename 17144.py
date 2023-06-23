from collections import deque
import copy

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def step1(graph) :
    graph2 = copy.deepcopy(graph)
    for i in range(r) :
        for j in range(c) :
            num = graph[i][j]
            if num < 5 :
                continue
            add = num // 5
            for k in range(4) :
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<r and 0<=nj<c and graph[ni][nj]!= -1:
                    graph2[i][j] -= add
                    graph2[ni][nj] += add
    return graph2

def step2(graph) :
    graph2 = copy.deepcopy(graph)
    flag = False
    for i in range(r) :
        for j in range(c) :
            if graph2[i][j] == -1 and not flag:
                flag = True
                graph2[i][1] = 0
                for k in range(2,c) :
                    graph2[i][k] = graph[i][k-1]
                for k in range(i,0,-1) :
                    graph2[k-1][c-1] = graph[k][c-1]
                for k in range(c-1,0,-1) :
                    graph2[0][k-1] = graph[0][k]
                for k in range(r) :
                    if graph2[k+1][0] == -1 :
                        break
                    graph2[k+1][0] = graph[k][0]
            if graph2[i][j] == -1 and flag:
                graph2[i][1] = 0
                for k in range(2, c):
                    graph2[i][k] = graph[i][k - 1]
                for k in range(i,r-1) :
                    graph2[k+1][c-1] = graph[k][c-1]
                for k in range(c-1,0,-1) :
                    graph2[r-1][k-1] = graph[r-1][k]
                for k in range(r-1,1,-1) :
                    if graph2[k-1][0] == -1 :
                        break
                    graph2[k-1][0] = graph[k][0]
    return graph2
if __name__ == '__main__':

    r,c,t = map(int, input().split())
    graph = list()
    for i in range(r) :
        graph.append(list(map(int, input().split())))
    for _ in range(t) :
        graph = step1(graph)
        graph = step2(graph)
    total_sum = sum(sum(row) for row in graph)
    print(total_sum+2)