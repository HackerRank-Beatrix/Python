import numpy

arr = list(map(int, input().split(' ')))
print(numpy.array(arr).reshape(3, 3))