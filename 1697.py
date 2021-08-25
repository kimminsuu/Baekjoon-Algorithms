from collections import deque

n, k = map(int, input().split())
max = 100001
past = list()

count = 0
queue = deque()
queue.append(n)
queue.append(-1)
past.append(n)

while queue :
    x = queue.popleft()
    if x == -1 :
        count+=1
        queue.append(x)
        continue
    if x == k :
        print(count)
        break
    if x-1 not in past and x-1 >=0:
        queue.append(x-1)
        past.append(x-1)
    if x+1 not in past and x+1 < max:
        queue.append(x+1)
        past.append(x+1)
    if 2*x not in past and 2*x < max:
        queue.append(2*x)
        past.append(2*x)
        
