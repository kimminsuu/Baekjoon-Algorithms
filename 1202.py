import sys
import heapq
input = sys.stdin.readline

N,K = map(int,input().split())
arr = list()
_max = list()
for _ in range(N) :
    arr.append(list(map(int,input().split())))
for _ in range(K) :
    _max.append(int(input()))

arr.sort(key=lambda x:(x[0],-x[1]))
_max.sort()

ans = []
idx = 0
tot=0
for i in range(len(_max)) :
    while idx <= len(arr)-1 and _max[i] >= arr[idx][0] :
        heapq.heappush(ans,-arr[idx][1])
        idx+=1
    if ans :
        tot -= heapq.heappop(ans)
print(tot)
