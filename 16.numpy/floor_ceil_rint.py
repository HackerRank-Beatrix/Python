import numpy

numpy.set_printoptions(sign=' ')

arr = list(map(float, input().split(' ')))
arr = numpy.array(arr)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))