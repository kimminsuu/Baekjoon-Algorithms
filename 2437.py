import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int,read().split()))
arr.sort()
num = 1
for i in range(n) :
    if num < arr[i] :
        break
    num+=arr[i]
print(num)
