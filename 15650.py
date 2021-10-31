import sys
read = sys.stdin.readline
from itertools import combinations

n,m = map(int,read().split())
for i in list(combinations(range(1,n+1),m)) :
    print(' '.join(map(str,i)))
    
