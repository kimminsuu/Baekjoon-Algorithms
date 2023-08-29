from collections import deque

if __name__=='__main__' :
    N = int(input())
    arr = []
    for i in range(N) :
        arr.append(list(map(int,input().split())))
    arr.sort(key=lambda x:x[1])
    idx = -1
    ans = 0
    for c in arr:
        if idx <= c[0] :
            idx = c[1]
            ans+=1
    print(ans)