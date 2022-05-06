import random

arr = list()
a1,a2,a3,a4,a5 = 0,0,0,0,0
for _ in range(200) :
    num = random.randrange(1,101)
    arr.append(num)
    if num>0 and num<=20 :
        a1+=1
    elif num>20 and num<=40:
        a2+=1
    elif num>40 and num<=60:
        a3+=1
    elif num>60 and num<=80:
        a4+=1
    else :
        a5+=1
arr.sort()

for i in range(10) :
    for j in range(20) :
        print("{0:4}".format(arr[20*i+j]), end='')
    print('\n')

print("-----------------------\n")
print(" 1 -  20:", end=' ')
for i in range(a1) :
    print('*',end='')
print("   ",end='')
print(a1)
print("20 -  40:", end=' ')
for i in range(a2) :
    print('*',end='')
print("   ",end='')
print(a2)
print("40 -  60:", end=' ')
for i in range(a3) :
    print('*',end='')
print("   ",end='')
print(a3)
print("60 -  80:", end=' ')
for i in range(a4) :
    print('*',end='')
print("   ",end='')
print(a4)
print("80 - 100:", end=' ')
for i in range(a5) :
    print('*',end='')
print("   ",end='')
print(a5)

