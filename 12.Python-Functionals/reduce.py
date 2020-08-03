#https://www.hackerrank.com/challenges/reduce-function/problem

from fractions import Fraction
from functools import reduce
import math

def product(fracs):
    t = reduce(lambda x, y: Fraction(x.numerator*y.numerator, x.denominator*y.denominator), fracs)

    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)