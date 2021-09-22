import sys
read = sys.stdin.readline

x, y = map(int,read().split())
z = (y * 100) // x

if z >= 99 :
    print(-1)
else :
    start, end = 1, x
    ans = 0

    while start <= end :
        mid = (start+end) //2
        if (y+mid)*100 // (x+mid) >z :
            ans = mid
            end = mid - 1
        else :
            start = mid + 1
    print(ans)
