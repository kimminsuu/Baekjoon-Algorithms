''' #이건 겹치는 선이 총 몇개 그어져야하나
N = int(input())
arr = list()

for _ in range(N) :
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x: (x[1], -x[0]))
ans = 0
idx = -1
for i in range(len(arr)) :
    if idx <= arr[i][0] :
        ans+=1
        idx = arr[i][1]
print(ans)
'''
import sys
from collections import deque
read = sys.stdin.readline()

N = int(read().rstrip())
arr = []
for _ in range(N):
    a,b = map(int,input().rstrip().split())
    arr.append((a,1)) # 선분 시작
    arr.append((b,-1)) # 선분 끝

arr.sort()
tot = 0
cnt = 0

for _ , point in arr:
    cnt += point
    tot = max(tot,cnt)

print(tot)