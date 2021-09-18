import sys
read = sys.stdin.readline

n = int(read())
have = list(map(int,read().split()))
m = int(read())
check = list(map(int,read().split()))
have.sort()

for i in range(m) :
    start, end = 0,n-1
    while start <= end :
        mid = start+end //2
        if have[mid] == check[i] :
            print(1, end=" ")
            break
        elif have[mid] < check[i] :
            start = mid + 1
        else :
            end = mid - 1

        if start > end :
            print(0, end = " ")
            break
