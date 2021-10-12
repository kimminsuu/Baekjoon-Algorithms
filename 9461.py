import sys
read = sys.stdin.readline

nums = [0] * 101
nums[1] = 1
nums[2] = 1
nums[3] = 1
for i in range(4, 101) :
    nums[i] = nums[i-2] + nums[i-3]

n = int(read())
for _ in range(n) :
    k = int(read())
    print(nums[k])
    
