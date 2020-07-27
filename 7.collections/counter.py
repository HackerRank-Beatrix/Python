#https://www.hackerrank.com/challenges/collections-counter/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    shoe_sizes = input().split()
    num_of_cust = int(input())

    shoe_count = Counter(map(int, shoe_sizes))

    money_earned = 0
    for i in range(num_of_cust):
        sz, val = map(int, input().split())
        if shoe_count[sz] is not None and shoe_count[sz] != 0:
            shoe_count[sz] = shoe_count[sz] - 1
            money_earned += val
    print(money_earned)
