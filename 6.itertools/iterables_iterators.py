#https://www.hackerrank.com/challenges/iterables-and-iterators/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    k = int(input())

    index = []
    for i in range(len(arr)):
        if arr[i] == 'a':
            index.append(i + 1)
    combs = list(combinations(range(1, len(arr) + 1), k))

    count = 0
    for i in range(len(combs)):
        for j in range(k):
            if combs[i][j] in index:
                count += 1
                break

    print('{:}'.format(count / len(combs)))
