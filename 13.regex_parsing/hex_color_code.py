#https://www.hackerrank.com/challenges/hex-color-code/problem

import re

HEX_PATTERN = re.compile(r'(?<!^)(#(?:[\dA-Fa-f]{3}){1,2})')

for _ in range(int(input())):
    s = input()
    m = HEX_PATTERN.findall(s)
    for i in m:
        print(i)