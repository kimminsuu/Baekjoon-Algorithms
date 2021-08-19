n = int(input())
arr = []
for i in range(n) :
	start, end = map(int, input().split())
	arr.append([start,end])

arr = sorted(arr, key = lambda a:a[0])
arr = sorted(arr, key = lambda a:a[1])

end_t, count = 0, 0
for a in arr :
	if a[0] >= end_t :
		count+=1
		end_t = a[1]
print(count)
