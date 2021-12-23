import sys
read = sys.stdin.readline

n = int(read())
case = []
Tn = []
s = 0
for i in range(45) :
    s += i+1
    Tn.append(s)

for i in Tn :
    for j in Tn :
        for k in Tn :
            if i+j+k <= 1000 :
                case[i+j+k] = 1

for _ in range(n) :
    print(case[int(read())])
