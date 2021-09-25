import sys
read = sys.stdin.readline

n,c = map(int,read().split())
house = []
for _ in range(n) :
    house.append(int(read()))

house.sort()

start,end = 1, house[-1]-house[0]
res = 0

while(start<=end) :
    mid = (start+end) // 2
    cur = house[0]
    count = 1

    for i in range(1, len(house)) :
        if house[i] >= cur+mid :
            count+=1
            cur = house[i]

    if count >= c :
        start = mid + 1
        res = mid
    else :
        end = mid - 1

print(res)
