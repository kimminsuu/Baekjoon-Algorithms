import sys
read = sys.stdin.readline

n = int(read())
s = list()
for _ in range(n) :
    s.append(int(read()))
s.sort()

for i in range(n) :
    s[i] *= n-i

print(max(s))
