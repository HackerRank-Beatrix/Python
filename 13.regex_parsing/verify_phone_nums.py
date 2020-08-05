#https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

if __name__ == '__main__':
    for _ in range(int(input())):
        result = bool(re.match(r'^[789]\d{9}$', input()))
        print('YES' if result else 'NO')