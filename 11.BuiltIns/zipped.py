#hackerrank.com/challenges/zipped/problem

if __name__ == '__main__':
    N, X = map(int, input().split())

    marks = []
    for i in range(X):
        marks.append(list(map(float, input().split())))

    for item in zip(*marks):
        print(sum(item) / len(item))