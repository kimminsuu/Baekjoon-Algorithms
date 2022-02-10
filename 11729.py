import sys

def func(num,one,two,three) :
    if num == 1 :
        order.append((one,three))
        return
    else :
        func(num-1,one,three,two)
        order.append((one,three))
        func(num-1,two,one,three)

n = int(input())
order = list()
func(n,1,2,3)

print(len(order))
print(
