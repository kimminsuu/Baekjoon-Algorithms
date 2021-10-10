import sys
read = sys.stdin.readline

n = int(read())
s = [0, 1, 1]
for i in range(3, 91):
  s.append(s[i-1] + s[i-2])
print(s[n])
