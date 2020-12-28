import numpy

n = int(input())

A, B = [], []
for _ in range(n):
    A.append(list(map(int, input().split())))
A = numpy.array(A)

for _ in range(n):
    B.append(list(map(int, input().split())))
B = numpy.array(B)

print(numpy.dot(A, B))