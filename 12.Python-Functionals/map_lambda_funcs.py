#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: pow(x, 3)

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

def fibonacci(n):
    result = []
    for i in range(n):
        result.append(fib(i))
    return result

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))