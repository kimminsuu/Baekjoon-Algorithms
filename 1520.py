import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if check[x][y] == -1:
        check[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if s[x][y] < s[nx][ny]:
                    check[x][y] += dfs(nx, ny)
    return check[x][y]
m, n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
check = [[-1] * n for i in range(m)]
print(dfs(m - 1, n - 1))
