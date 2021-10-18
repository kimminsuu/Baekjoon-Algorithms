import sys
from collections import deque
read = sys.stdin.readline

n,k = map(int,read().split())
queue = deque()
queue.append(n)

count = 0
check = [0] * 100001
check[n] = 1
while queue :
    x = queue.popleft()
    if x == k :
        count+=1
    
