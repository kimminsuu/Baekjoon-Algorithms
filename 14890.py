import sys
read = sys.stdin.readline

n,l = map(int,read().split())
graph = list()
for i in range(n) :
    graph.append(list(map(int,read().split())))

count = 1
s = list()

def func(s) :
    flag = [True] * n
    for i in range(n-1) :
        if s[i] == s[i+1] :
            continue
        elif abs(s[i]-s[i+1]) > 1 :
            return 0
        else :
            if s[i] > s[i+1] :
                for j in range(i+1,i+1+l) :
                    if 0<=j<n :
                        if s[j] != s[i+1] :
                            return 0
                        if not flag[j] :
                            return 0
                        flag[j] = False
                    else :
                        return 0
            else :
                for j in range(i,i-l,-1) :
                    if 0<=j<n :
                        if s[j] != s[i] :
                            return 0
                        if not flag[j] :
                            return 0
                        flag[j] = False
                    else :
                        return 0
    return 1
    

for i in range(n) :
    s = graph[i][:]
    count += func(s)
    s = graph[:][i]
    count += func(s)
print(count)
