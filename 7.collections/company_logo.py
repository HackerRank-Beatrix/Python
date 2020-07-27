#https://www.hackerrank.com/challenges/most-commons/problem

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

    result = dict()
    for c in s:
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1

    count = 3
    for val in sorted(set(result.values()), reverse=True):
        subresult = {k: v for k, v in result.items() if v == val}
        subresult = dict(sorted(subresult.items()))
        for k1, v1 in subresult.items():
            count -= 1
            if count <= -1:
                break
            print(k1, v1)
