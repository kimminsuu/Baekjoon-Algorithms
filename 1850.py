import sys
read = sys.stdin.readline

def func(a,b) :
    if b==0 :
        return a
    ans = a%b
    return func(b,ans)

a,b = map(int,read().split())
n = func(a,b)
print('1'*n)
