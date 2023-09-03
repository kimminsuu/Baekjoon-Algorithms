import sys
input = sys.stdin.readline
N = int(input())
arr = list()
for _ in range(N) :
    a,b=map(int,input().split())
    arr.append([a,1])
    arr.append([b,-1])
ans = 1
tot=0
arr.sort()
idx = arr[0][0]
for i in range(1,len(arr)):
    if arr[i][1] == 1 :
        ans+=1
    else :
        ans-=1
    tot = max(tot,ans)
print(tot)