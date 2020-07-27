#https://www.hackerrank.com/challenges/compress-the-string/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
if __name__ == '__main__':
    str = input()
    result = []
    for k, g in groupby(str):
        result.append((len(list(g)), int(k)))

    print(*result, sep=" ")