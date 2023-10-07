import sys
import heapq

input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

arr.sort()
hq=[]
heapq.heappush(hq,arr[0][1])
_max = 1

for i in range(1,N):
    while hq and arr[i][0] >=hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq,arr[i][1])
    _max = max(_max,len(hq))
print(_max)
