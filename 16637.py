from collections import deque

res = -2 ** 31 - 1

def calc(nums,ops) : #끝까지 계산
    while ops :
        num1 = nums.popleft()
        num2 = nums.popleft()
        op = ops.popleft()

        if op == '+' :
            num = num1 + num2
        elif op == '-' :
            num = num1 - num2
        else :
            num = num1 * num2

        nums.appendleft(num)

    return nums.pop()

def rec(num:int, nums, ops) :
    global res
    if num == 1 or len(nums) == 1 :
        res = max(res,calc(nums,ops))
        return

    rec(num-1,nums,ops)

    try :
        num1 = nums.popleft()
        num2 = nums.popleft()
        op = ops.popleft()
        if op == '+' :
            temp = num1 + num2
        elif op == '-' :
            temp = num1 - num2
        else :
            temp = num1 * num2
        nums.appendleft(temp)
        rec(num-1, nums, ops)
    except :
        0

    return max(res, calc(nums, ops))

if __name__ == "__main__" :
    n = int(input())
    s = input()

    nums = deque()
    ops = deque()

    for i in range(n):
        if i % 2 == 0:
            nums.append(int(s[i]))
        else:
            ops.append(s[i])

    num = len(ops)

    rec(num,nums,ops)
    print(res)
