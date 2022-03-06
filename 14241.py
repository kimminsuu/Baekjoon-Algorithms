n = int(input())
s = list(map(int,input().split()))

s.sort(reverse=True)

sum =0
score = 0
tot = 0

for i in range(0,n-1) :
    score = s[i]*s[i+1]
    s[i+1] = s[i]+s[i+1]
    tot = tot+score

print(tot)
