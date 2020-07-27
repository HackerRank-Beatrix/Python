#https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

if __name__ == '__main__':
    n = int(input())

    result = []
    for i in range(n):
        size = int(input())
        d = deque(map(int, input().split()))
        stack = []

        flag = 'Yes'
        while len(d) > 0:
            item = None
            if len(d) == 1:
                item = d.pop()
            else:
                l, r = d[0], d[-1]
                if l >= r:
                    item = d.popleft()
                else:
                    item = d.pop()

            if stack == [] or stack[-1] >= item:
                stack.append(item)
            else:
                flag = 'No'
                break

        result.append(flag)

    for r in result:
        print(r)


