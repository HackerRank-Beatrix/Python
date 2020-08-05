#https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

if __name__ == '__main__':
    S = input()
    k = input()
    m = re.search(k, S)
    pattern = re.compile(k)
    if not m: print("(-1, -1)")
    while m:
        print("({0}, {1})".format(m.start(),m.end()-1))
        m = pattern.search(S,m.start()+1)