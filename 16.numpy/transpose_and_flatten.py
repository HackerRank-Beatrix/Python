import numpy

rc = list(map(int, input().split(' ')))

arr = []
for i in range(rc[0]):
    arr.append(list(map(int, input().split(' '))))

arr = numpy.array(arr)
print(numpy.transpose(arr))
print(arr.flatten())