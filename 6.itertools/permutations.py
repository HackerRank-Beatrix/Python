#https://www.hackerrank.com/challenges/itertools-permutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == '__main__':
    arg1, arg2 = input()
    p = int(arg2)

    for a in permutations(arg1, p):
        print(a)
