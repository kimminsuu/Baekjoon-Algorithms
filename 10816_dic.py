import sys
read = sys.stdin.readline

n = int(read())
have = list(map(int,read().split()))

dict1 = dict()
for i in have :
    if i in dict1 :
        dict1[i]+=1
    else :
        dict1[i] = 1

m = int(read())
check = list(map(int,input().split()))

for i in check :
    if i in dict1 :
        print(dict1[i], end=' ')
    else :
        print(0, end = ' ')
