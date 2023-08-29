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
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    res = 0
    for i in range(1, n):
        mn = min(a[i], a[i - 1])
        mx = max(a[i], a[i - 1])
        while mx > 2 * mn:
            res += 1
            mn *= 2
    print(res)



