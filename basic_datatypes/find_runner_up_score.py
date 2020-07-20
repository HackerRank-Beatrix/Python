#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
def runner_up(arr):
    arr = list(arr)
    arr.sort()
    return arr[len(arr) - 2]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runner_up(set(arr)))