import sys
read = sys.stdin.readline

n = int(read())
alist, blist, clist, dlist = list(), list(), list(), list()
for  _ in range(n) :
    a,b,c,d = map(int, read().split())
    alist.append(a)
    blist.append(b)
    clist.append(c)
    dlist.append(d)

ab, cd = {}, {}
for a in alist :
    for b in blist :
        if not ab.get(a+b) :
            ab[a+b] = 1
        else :
            ab[a+b] += 1

for c in clist :
    for d in dlist :
        if not cd.get(c+d) :
            cd[c+d]=1
        else :
            cd[c+d]+=1

