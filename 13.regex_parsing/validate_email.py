#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re

if __name__ == '__main__':
    for _ in range(int(input())):
        name, email = input().split()
        result = re.match(r'<[a-zA-Z]+[\w_\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>', email)

        if result:
            print(name, email)