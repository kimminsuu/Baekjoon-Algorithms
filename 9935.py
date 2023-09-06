s = str(input())
arr=[]
bomb = list(map(str,input()))

for i in range(len(s)) :
    arr.append(s[i])
    while len(arr) >= len(bomb) :
        if arr[-len(bomb):] != bomb :
            break
        else :
            for _ in range(len(bomb)):
                arr.pop()
if arr :
    print(''.join(arr))
else :
    print("FRULA")

