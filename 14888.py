import sys
read = sys.stdin.readline

n = int(read())
s = list(map(int,read().split()))
fun = list(map(int,read().split()))

def dfs(count, res, p, m, mul, div, maxx, minn) :
    if count == n :
        maxx = max(maxx,res)
        minn = min(minn,res)
        return
    if p :
        dfs(count+1,res+s[count],p-1,m,mul,div,maxx,minn)
    if m :
        dfs(count+1,res-s[count],p,m-1,mul,div,maxx,minn)
    if mul :
        dfs(count+1,res*s[count],p,m,mul-1,div,maxx,minn)
    if div :
        dfs(count+1,-(-res//s[count]) if res<0 else res//s[count],p,m,mul,div-1,maxx,minn)

maxx = -1000000001
minn = 1000000001
dfs(1,s[0],fun[0],fun[1],fun[2],fun[3])
print(maxx)
print(minn)
