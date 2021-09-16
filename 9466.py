import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline


def dfs(x):
    global ans
    visit[x] = True
    cycle.append(x)
    num = arr[x]

    if visit[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


t = int(read())

for _ in range(t):
    n = int(read())
    arr = [0] + list(map(int,read().split()))
    visit = [False] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if not visit[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))
