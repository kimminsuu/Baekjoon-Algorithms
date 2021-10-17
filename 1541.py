import sys
read = sys.stdin.readline

n = read().split('-')
arr = list()
for i in n :
    a=0
    s = i.split('+')
    for j in s :
        a+=int(j)
    arr.append(a)
res = arr[0]
for i in range(1,len(arr)) :
    res -= arr[i]
print(res)
