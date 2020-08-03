#https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

if __name__ == '__main__':
    for i in range(int(input())):
        n = input()
        print(re.match("^[+-]?[0-9]*\.[0-9]+$", n) != None)

