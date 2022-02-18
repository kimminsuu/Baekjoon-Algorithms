import sys
read = sys.stdin.readline

n,m = map(int,read().split())
graph = [list(map(str,read().strip('\n'))) for _ in range(n)]
ans = list()

for i in range(n-7) :
    for j in range(m-7) :
        a,b = 0,0
        for k in range(i,i+8) :
            for l in range(j,j+8) :
                if (k+l)%2==0 :
                    if graph[k][l] == 'W' :
                        a+=1
                    if graph[k][l] == 'B' :
                        b+=1
                else :
                    if graph[k][l] == 'B' :
                        a+=1
                    if graph[k][l] == 'W' :
                        b+=1
            ans.append(a)
            ans.append(b)

print(min(ans))
