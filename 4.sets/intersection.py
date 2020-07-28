#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

if __name__ == '__main__':
    n1 = input()
    l1 = set(map(int, input().split()))
    n2 = input()
    l2 = set(map(int, input().split()))

    print(len(l1.intersection(l2)))