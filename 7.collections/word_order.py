#https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())

    d = OrderedDict()
    for i in range(n):
        key = input().strip()
        if key in d:
            d[key] = d.get(key) + 1
        else:
            d[key] = 1

    print(len(d.keys()))
    print(' '.join([str(e) for e in d.values()]))
