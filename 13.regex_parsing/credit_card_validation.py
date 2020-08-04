#https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

if __name__ == '__main__':
    PATTERN_16_DIGITS = re.compile(
        r'^'
        r'\d{16}'
        r'$'
    )

    PATTERN_START = re.compile(
        r'^'
        r'[456]'
    )

    PATTERN_HIPHEN = re.compile(
        r'^'
        r'(\d{4}-){3}\d{4}'
        r'$'
    )

    PATTERN_REPEAT = re.compile(
        r'([\d])\1\1\1'
    )

    for _ in range(int(input())):
        n = input()
        print("Valid" if (PATTERN_START.search(n) and (
                    PATTERN_16_DIGITS.search(n) or PATTERN_HIPHEN.search(n)) and not PATTERN_REPEAT.search(
            n.replace('-', ""))) else "Invalid")