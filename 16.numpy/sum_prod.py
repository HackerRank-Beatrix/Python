import numpy

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)
s = numpy.sum(arr, axis=0)
print(numpy.prod(s, axis=0))