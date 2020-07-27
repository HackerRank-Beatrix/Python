#https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        _ = input()
        a = set(map(int, input().split()))
        _ = input()
        b = set(map(int, input().split()))

        print(len(a.difference(b)) == 0)
