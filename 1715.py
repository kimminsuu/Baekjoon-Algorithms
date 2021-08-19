import sys
import heapq

n = int(input())
nums = []
for i in range(n) :
	heapq.heappush(nums, int(input()))
result = 0
if not len(nums) == 1 :
	while(len(nums) >1) :
		temp = heapq.heappop(nums)
		temp += heapq.heappop(nums)
		heapq.heappush(nums, temp)
		result+=temp
print(result)
