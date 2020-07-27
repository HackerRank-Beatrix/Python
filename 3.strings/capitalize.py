#https://www.hackerrank.com/challenges/capitalize/problem

# !/bin/python3

import math
import os
import random
import re
import sys
import string


# Complete the solve function below.
def solve(s):
    result = ''
    prev_space = True
    for i in range(len(s)):
        if s[i].isalpha():
            if prev_space:
                result += s[i].capitalize()
                prev_space = False
            else:
                result += s[i]

        else:
            if s[i] == ' ':
                prev_space = True
            else:
                prev_space = False
            result += s[i]

    print(result)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
