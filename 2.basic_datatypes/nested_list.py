#https://www.hackerrank.com/challenges/nested-list/problem
from collections import defaultdict

if __name__ == '__main__':
    students = defaultdict(list)
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[score].append(name)

    students = dict(sorted(students.items(), key=lambda x: x[0]))
    result = students[list(students.keys())[1]]
    result = sorted(result)
    for r in result:
        print(r)