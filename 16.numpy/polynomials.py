import numpy

c = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(c, x))