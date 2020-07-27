#https://www.hackerrank.com/challenges/polar-coordinates/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

if __name__ == '__main__':
    z = input()

    print(*cmath.polar(complex(z)), sep="\n")