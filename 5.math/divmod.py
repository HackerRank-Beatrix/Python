#https://www.hackerrank.com/challenges/python-mod-divmod/problem

if __name__ == '__main__':
    n1 = int(input())
    n2 = int(input())

    print(n1//n2)
    print(n1 % n2)
    print(divmod(n1, n2))