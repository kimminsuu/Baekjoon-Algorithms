import sys
from collections import deque
read = sys.stdin.readline

n,k = map(int,read().split())
queue = deque()
queue.append(n)

count = 0
check = [-1] * 100001
check[n] = 1
while queue :
    x = queue.popleft()
    if x == k :
        count+=1
    for i in [x+1, x-1, 2*x] :
        if 0<=i<100001 :
            if check[i]==-1 or check[i]>=check[x]+1 :
                check[i] = check[x]+1
                queue.append(i)
print(check[k])
print(count)
    
