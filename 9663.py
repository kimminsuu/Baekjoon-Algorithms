n = int(input())
row = [0]*n
res = 0

def func(x) :
    for i in range(x) :
        if row[x]==row[i] or abs(row[x]-row[i]) == x-i :
            return False
    return True

def dfs(x) :
    global res
    if x == n :
        res += 1
    else :
        for i in range(n) :
            row[x] = i
            if func(x) :
                dfs(x+1)

dfs(0)
print(res)
