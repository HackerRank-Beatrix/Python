import numpy

n, m = map(int, input().split(' '))

arr1, arr2 = [], []

for i in range(n):
    arr1.append(list(map(int, input().split(' '))))
arr1 = numpy.array(arr1, dtype=numpy.int)

for i in range(n):
    arr2.append(list(map(int, input().split(' '))))
arr2 = numpy.array(arr2, dtype=numpy.int)

print(numpy.add(arr1, arr2))
print(numpy.subtract(arr1, arr2))
print(numpy.multiply(arr1, arr2))
print(numpy.divide(arr1, arr2).astype(numpy.int))
print(numpy.mod(arr1, arr2))
print(numpy.power(arr1, arr2))