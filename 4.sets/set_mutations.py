#https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == '__main__':
    n = input()
    a = set(map(int, input().split()))

    for i in range(int(input())):
        command, val = input().split()
        b = set(map(int, input().split()))

        if command == 'intersection_update':
            a.intersection_update(b)
        elif command == 'update':
            a.update(b)
        elif command == 'symmetric_difference_update':
            a.symmetric_difference_update(b)
        elif command == 'difference_update':
            a.difference_update(b)
        else:
            raise ValueError('Invalid command')

    print(sum(a))
