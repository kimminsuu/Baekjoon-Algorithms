import sys
read = sys.stdin.readline

n = int(read())
s = list(map(int,read().split()))
s.sort()

start, end = 0, n-1
res = end - start
ans = list()
while start < end :
    left = s[start]
    right = s[end]

    if abs(left+right) < res :
        res = abs(left+right)
        ans = [left, right]

    if left+right < 0 :
        start += 1
    else :
        end -= 1
print(ans[0], ans[1])
    
