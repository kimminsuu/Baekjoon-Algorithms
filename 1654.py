import sys
read = sys.stdin.readline

k,n = map(int, read().split())
lan = [int(read()) for _ in range(k)]
start, end = 1, max(lan)

while start <= end :
    mid = (start+end) //2
    count = 0
    for i in lan :
        count += i//mid

    if count >= n :
        start = mid + 1
    else :
        end = mid - 1
print(end)
