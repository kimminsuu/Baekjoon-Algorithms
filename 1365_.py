import sys
import bisect

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

LIS = [num[0]]
for n in num[1:]:
    if LIS[-1] < n:
        LIS.append(n)
    else:
        tmp = bisect.bisect_left(LIS, n)
        LIS[tmp] = n

print(N-len(LIS))
