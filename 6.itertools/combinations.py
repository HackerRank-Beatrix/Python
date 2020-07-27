#https://www.hackerrank.com/challenges/itertools-combinations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    s, limit = input().split(maxsplit=1)
    limit = int(limit)

    for i in range(1, limit+1):
        for j in combinations(sorted(s), i):
            print(''.join(j))
