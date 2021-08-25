from collections import deque

n, k = map(int, input().split())
max = 100001
past = [0] * max

count = 0
queue = deque()
queue.append(n)

while queue :
    x = queue.popleft()
    if x == k :
        print(past[x])
        break
    for nx in (x+1,x-1,2*x) :
        if 0<=nx<max and not past[nx] :
            past[nx] = past[x] + 1
            queue.append(nx)
        
