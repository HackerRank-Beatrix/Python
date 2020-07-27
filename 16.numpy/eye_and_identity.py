#https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy

dim = list(map(int, input().split()))
numpy.set_printoptions(formatter={'all':lambda x: ' ' + str(x).rstrip('0')})
print(numpy.eye(dim[0], dim[1]))