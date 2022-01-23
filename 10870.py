n = int(input())

def f(num) :
    if num<=1 :
        return num
    return f(num-1)+f(num-2)

print(f(n))
