#hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
if __name__ == '__main__':

    d = deque()
    for i in range(int(input())):
        inputs = input().split()
        command = inputs[0]
        val = None
        if len(inputs) == 2:
            val = inputs[1]

        if command == 'append':
            d.append(val)
        elif command == 'pop':
            d.pop()
        elif command == 'appendleft':
            d.appendleft(val)
        elif command == 'popleft':
            d.popleft()
        else:
            raise ValueError('Invalid Command')

    for item in d:
        print(item, end = ' ')
