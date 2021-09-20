import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

n = int(read())
have = list(map(int, read().split()))
m = int(read())
check = list(map(int,read().split()))
have.sort()
arr = [0] * m

for i in range(m) :
    start,end = 0,n-1
    while start <= end :
        mid = (start+end) // 2
        if check[i] == have[mid] :
            arr[i]+=1
            break
        elif have[mid] < check[i] :
            start = mid + 1
        else :
            end = mid - 1

        if start > end :
            break

