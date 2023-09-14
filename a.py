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

from decimal import Decimal
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
    
class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def isInvalid(self):
        c1 = Point.distance(self.x, self.y)
        c2 = Point.distance(self.z, self.y)
        c3 = Point.distance(self.x, self.z)
        return ("%.3f" % (c1 + c2 + c3)) if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1 else "INVALID"

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        p3 = Point(Decimal(arr[4]), Decimal(arr[5]))
        tg = Triangle(p1, p2, p3)
        print(tg.isInvalid())