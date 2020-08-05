#https://www.hackerrank.com/challenges/re-group-groups/problem

import re

if __name__ == '__main__':
    n = input().strip()
    m = re.search(
        r'([a-zA-Z0-9])\1+', n
    )

    print(m.group(1) if m else -1)