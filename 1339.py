n = int(input())
words = []
for i in range(n) :
	words.append(input())
d = {}
for word in words :
	j = len(word) - 1
	for k in word :
		if k in d :
			d[k] += pow(10, j)
		else :
			d[k] = pow(10,j)
		j-=1
nums = []
for v in d.values() :
    nums.append(v)
nums.sort(reverse = True)
result = 0
time = 9
for i in range(len(nums)) :
	result += nums[i] * time
	time-=1
print(result)
