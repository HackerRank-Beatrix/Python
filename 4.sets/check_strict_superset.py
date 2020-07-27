#https://www.hackerrank.com/challenges/py-check-strict-superset/problem

if __name__ == '__main__':
    a = set(map(int, input().split()))
    n = int(input())

    flag = True
    for i in range(n):
        b = set(map(int, input().split()))
        if not len(b.difference(a)) == 0:
            flag = False

    print(flag)
