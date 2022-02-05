import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)


n = int(read())
tree = [[] for _ in range(n+1)]
p = [0 for _ in range(n+1)]

for i in range(n-1) :
    a,b = map(int,read().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(x,tree,p) :
    for i in tree[x] :
        if p[i] ==0 :
            p[i] = x
            dfs(i,tree,p)

dfs(1,tree,p)
for i in range(2,n+1) :
    print(p[i])
