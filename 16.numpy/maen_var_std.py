import numpy
n, m = map(int, input().split(" "))
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr, dtype=numpy.int)

numpy.set_printoptions(sign="-")
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.around(numpy.std(arr), 11))