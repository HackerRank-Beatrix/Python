#https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    stamps = set()
    for i in range(n):
        stamps.add(input())

    print(len(stamps))
