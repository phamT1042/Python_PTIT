# import sys
# def stdin_gen():
#     for x in sys.stdin.read().split():
#         yield int(x)
# cin = stdin_gen()

# import sys
# i = 0
# t = int(input())
# for line in sys.stdin:
#     n = int(line)
#     i += 1
#     if i == t: break

#for _ in range(int(sys.stdin.readline())):

#memory with array < memory with list
from math import sqrt

mx = 8000
sang = [1] * mx
sang[0] = sang[1] = 0
for i in range(2, int(sqrt(mx)) + 1):
    if sang[i]:
        for j in range(i * i, mx, i): sang[j] = 0
    
prime = [0]
for i in range(mx): 
    if sang[i]: prime.append(i)

n, x = map(int, input().split())
for i in range(n + 1):
    x += prime[i]
    print(x, end = ' ')
