from collections import defaultdict
#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    students = defaultdict(list)
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        students[name] = scores
    query_name = input()

    print("{:.2f}".format(sum(students[query_name])/len(students[query_name])))