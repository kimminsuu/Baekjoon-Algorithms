import sys
read = sys.stdin.readline

n = int(read())
s = [0] * 301
arr = [0]*301

for i in range(n) :
    s[i] = int(read())

arr[0] = s[0]
arr[1] = s[0] + s[1]
arr[2] = max(s[0] + s[2] , s[1] + s[2])

for i in range(3,n) :
    arr[i] = max(arr[i-3]+s[i-1]+s[i], arr[i-2]+s[i])
print(arr[n-1])
