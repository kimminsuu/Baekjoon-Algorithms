import sys
read = sys.stdin.readline

n,m,d = map(int,read().split())
board = list()
for i in range(n) :
    board.append(list(map(int,read().split())))

def simul(positions) :
    s_board = [line[:] for line in board]
    killed_amount = 0
    

mmax = 0
for i in range(m) :
    for j in range(i+1,m) :
        for k in range(j+1,m) :
            mmax = max(mmax,simul((i,j,k)))

