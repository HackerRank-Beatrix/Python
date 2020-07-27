#https://www.hackerrank.com/challenges/exceptions/problem

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        try:
            a = list(map(int, input().split()))
            print(a[0]//a[1])
        except (ValueError, ZeroDivisionError) as e:
            print("Error Code:",e)
