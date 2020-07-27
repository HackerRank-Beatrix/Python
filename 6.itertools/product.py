#https://www.hackerrank.com/challenges/itertools-product/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for item in list(product(A, B)):
        print(item, end=" ")
