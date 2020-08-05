#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

def subs(match):
    if match.group() == '||':
        return 'or'
    elif match.group() == '&&':
        return 'and'
    else:
        return ' '

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )', subs, input()))