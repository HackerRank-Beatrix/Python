#https://www.hackerrank.com/challenges/incorrect-regex/problem

import re
if __name__ == '__main__':
    for i in range(int(input())):
        result = True
        try:
            exp = re.compile(input())
        except Exception as e:
            result = False
        print(result)