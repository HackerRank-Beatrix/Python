#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())

    ind = 0
    d = defaultdict(list)
    for i in range(n):
        key = input()
        ind += 1
        d[key].append(ind)

    for j in range(m):
        key = input()
        val = d[key]

        if val == []:
            print(-1)
        else:
            print(*val)