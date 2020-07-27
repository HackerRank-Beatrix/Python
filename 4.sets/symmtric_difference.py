#https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    m = int(input())
    s1 = set(map(int, input().split()))
    n = int(input())
    s2 = set(map(int, input().split()))

    common_items = s1.intersection(s2)
    result = sorted(s1.difference(common_items).union(s2.difference(common_items)))

    for i in range(len(result)):
        print(result[i])