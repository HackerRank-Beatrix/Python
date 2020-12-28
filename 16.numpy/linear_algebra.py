import numpy

n = int(input())

A = []

for _ in range(n):
    A.append(list(map(float, input().split())))
A = numpy.array(A)

print(numpy.around(numpy.linalg.det(A), 2))