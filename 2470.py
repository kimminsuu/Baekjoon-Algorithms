import sys
read = sys.stdin.readline

n = int(read())
s = list(map(int,read().split()))

s.sort()
left, right = 0 , n-1
ans = s[left]+s[right]
start= left
end = right
while left < right :
    mid = s[left]+s[right]
    if abs(mid) < abs(ans) :
        ans = mid
        start = left
        end = right
        if ans == 0:
            break

    if mid < 0 :
        left += 1
    else :
        right -= 1

print(s[start],s[end])
