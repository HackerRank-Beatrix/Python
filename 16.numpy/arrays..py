import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    return numpy.array(arr, dtype=numpy.float64)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)