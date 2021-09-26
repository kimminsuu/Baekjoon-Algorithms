import sys
read = sys.stdin.readline

n,m = map(int, read().split())
tree = list(map(int,read().split()))
tree.sort()

start, end = tree[0], tree[-1]

while start <= end :
    result = 0
    mid = (start+end) // 2
    for i in range(n) :
        if tree[i] - mid > 0 :
            result += tree[i] - mid

    if result >= m :
        start = mid + 1
    else :
        end = mid - 1

print(end)
