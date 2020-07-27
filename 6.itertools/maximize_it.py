#https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

if __name__ == '__main__':
    n, m = map(int, input().split())

    lists = []
    for i in range(n):
        size, *lst = map(int, input().split())
        lists.append(lst)

    result = 0
    for item in product(*lists):
        s = 0
        for it in item:
            s += it * it
        s = s % m

        if s > result:
            result = s

    print(result)
