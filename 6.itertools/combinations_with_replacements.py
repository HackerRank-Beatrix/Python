#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, n = input().split()
    s = sorted(s)
    n = int(n)

    result = combinations_with_replacement(s, n)

    for item in result:
        print(''.join(item))