t = int(input())
for i in range(t) :
    a=[]
    n = int(input())
    for j in range(2) :
        a.append(list(map(int,input().split())))
    for k in range(1,n) :
        if k == 1 :
            a[0][k] += a[1][k-1]
            a[1][k] += a[0][k-1]
        else :
            a[0][k] += max(a[1][k-1], a[1][k-2])
            a[1][k] += max(a[0][k-1], a[0][k-2])
    print(max(a[0][n-1], a[1][n-1)))
