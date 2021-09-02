import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
a,b = map(int,read().split())
m = int(read())
dict = {}
for i in range(n) :
    dict[i+1] = set()
for _ in range(m) :
    x,y = map(int, read().split())
    dict[x].add(y)
    dict[y].add(x)

queue = deque()
queue.append(a)
count = 0
state = [0] * (n+1)
'''
while queue :
    num = queue.popleft()
    if num == b :
        break
    if state[num] == 0 :
        for n in dict[num] :
            if state[n] == 0 :
                queue.append(n)
                state[num]+=1
                state[n] = state[num]+1
print(state[num])
'''
num = queue.popleft()
set = dict[num]
for n in set :
    queue.append(n)
    dict[num].remove(n)
