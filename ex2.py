from collections import deque

N = int(input())
arr = list(map(int,input().split()))

q = deque()
ans = [-1] * N
for i in range(N) :
    while q and arr[q[-1]] < arr[i] :

        tmp = q.pop()
        ans[tmp] = arr[i]
    q.append(i)

print(*ans)
#for i in ans :
#    print(i, end=' ')
