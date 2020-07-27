#https://www.hackerrank.com/challenges/py-set-union/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n1 = input()
    e = set(map(int , input().split()))
    n2 = input()
    f = set(map(int, input().split()))

    print(len(e.union(f)))
