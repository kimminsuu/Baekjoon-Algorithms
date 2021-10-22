import sys
read = sys.stdin.readline

n = int(read())
res = 0
for i in range(1,n+1) :
    nums = list(map(int, str(i)))
    res = i +sum(nums)
    if res == n :
        print(i)
        break
    if i == n :
        print(0)
