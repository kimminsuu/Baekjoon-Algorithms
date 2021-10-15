import sys
read = sys.stdin.readline

x = int(read())
s = list(map(int,read().split()))
rev = s[::-1]

inc = [1] * x
dec = [1] * x

for i in range(x) :
    for j in range(i) :
        if s[i] > s[j] :
            inc[i] = max(inc[i], inc[j]+1)
        if rev[i] > rev[j] :
            dec[i] = max(dec[i], dec[j]+1)

res = [0] * x
for i in range(x) :
    res[i] = inc[i] + dec[x-i-1] - 1

print(max(res))
