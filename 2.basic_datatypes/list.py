# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(N):
        command, *vals = input().split()

        if command == 'insert':
            vals = list(map(int, vals))
            result.insert(*vals)
        elif command == 'print':
            print(result)
        elif command == 'remove':
            vals = list(map(int, vals))
            result.remove(vals[0])
        elif command == 'append':
            vals = list(map(int, vals))
            result.append(vals[0])
        elif command == 'sort':
            result.sort()
        elif command == 'pop':
            result.pop()
        elif command == 'reverse':
            result.reverse()
        else:
            raise ValueError('Invalid command')