n,m = map(int,input().split())
s = []

def func(d, idx,n,m) :
    if d = m:
        print(' '.join(map(str, s)))
        return
    for i in range(idx,n) :
        s.append(i+1)
        func(d+1,i,n,m)
        s.pop()

func(0,0,n,m)
