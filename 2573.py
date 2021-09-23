import sys
read = sys.stdin.readline

n,m = map(int, read().split())
graph = list()
for _ in range(n) :
    graph.append(list(map(int, read().split())))

