import sys
read = sys.stdin.readline

n = int(read())
a = list(map(int, read().split()))
b = list(map(int, read().split()))
ans = 0

for _ in range(n) :
    ans += min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))
print(ans)
