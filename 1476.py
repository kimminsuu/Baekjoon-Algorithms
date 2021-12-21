import sys

e,s,m = map(int,input().split())
ee,ss,mm, cnt = 1,1,1,1


while(1) :
    if ee == e and ss == s and mm == m :
        break
    ee+=1
    ss+=1
    mm+=1
    cnt+=1
    if ee>=16 : ee-=15
    if ss>=29 : ss-=28
    if mm>=20 : mm-=19

print(cnt)
