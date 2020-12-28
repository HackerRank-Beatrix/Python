import numpy

N, M, P = map(int, input().split(' '))

array1 = []
array2 = []
for i in range(N):
    array1.append(list(map(int, input().split(' '))))

for i in range(M):
    array2.append(list(map(int, input().split(' '))))

array1 = numpy.array(array1)
array2 = numpy.array(array2)

print(numpy.concatenate((array1, array2), axis=0))