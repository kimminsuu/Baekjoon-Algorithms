w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

dx = [1,-1,1,-1]
dy = [1,1,-1,-1]

count = 0
direction = 0

while True :
    if t = count :
        break
    count+=1
    nx = p+dx[direction]
    ny = q+dy[direction]

    if nx<=0 or nx>=w :
        if direction == 0: direction = 1
        elif direction == 1 : direction = 0
        elif direction == 2 : direction = 3
        elif direction == 3 : direction = 2

    if ny <= 0 or ny>=h :
        if direction == 0: direction = 3
        elif direction == 1 : direction = 2
        elif direction == 2 : direction = 1
        elif direction == 3 : direction = 0

    p,q = nx,ny

print(p,q)
