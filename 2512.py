import sys
read = sys.stdin.readline

n = int(read())
money = list(map(int,read().split()))
m = int(read())
money.sort()

start, end = 0, max(money)
while start <= end :
    mid = (start+end) // 2
    val = 0
    for i in range(n) :
        if money[i] > mid :
            val += mid
        else :
            val += money[i]
    if val > m :
        end = mid-1
    else :
        start = mid + 1
print(end)
