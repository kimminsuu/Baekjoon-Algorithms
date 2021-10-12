import sys
read = sys.stdin.readline

n = int(read())
for _ in range(n) :
    a,b = map(int,read().split())
    asum, bsum = 1,1
    for i in range(1,a+1) :
        asum *= i
        bsum *= b-i+1
    print(bsum // asum)
