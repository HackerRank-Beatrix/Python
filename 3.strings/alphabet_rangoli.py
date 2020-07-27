#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    total_chars = (4 * size - 3)
    lst = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        lst.append((s[::-1] + s[1:]).center(total_chars, '-'))

    result = lst[-1:0:-1] + lst
    print("\n".join(result))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)