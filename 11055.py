n = int(input())
s = list(map(int,input().split()))

arr = [1] * n
arr[0] = s[0]
for i in range(1,n) :
    for j in range(i) :
        if s[j] < s[i] :
            arr[i] = max(arr[i],arr[j]+s[i])
        else :
            arr[i] = max(arr[i],s[i])
print(max(arr))
