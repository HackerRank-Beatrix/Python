#https://www.hackerrank.com/challenges/ginorts/problem

if __name__ == '__main__':
    n = input()

    print(*sorted(n, key=lambda x: (x.isdigit() and (int(x) % 2 == 0), x.isdigit() and (int(x) % 2 == 1), x.isupper(), x.islower(), x)), sep='')