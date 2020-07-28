#https://www.hackerrank.com/challenges/py-set-difference-operation/problem

if __name__ == '__main__':
    n1 = input()
    a = set(map(int, input().split()))
    n2 = input()
    b = set(map(int, input().split()))

    print(len(a.difference(b)))