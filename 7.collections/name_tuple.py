#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    cols = input().split()
    Student = namedtuple('Student', cols)

    students = []
    for i in range(n):
        data = list(map(str, input().split()))
        students.append(Student(*data))

    print(sum([int(std.MARKS) for std in students]) / n)
