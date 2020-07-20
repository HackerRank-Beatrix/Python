# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    result = tuple(map(int, input().split()))
    print(hash(result))
