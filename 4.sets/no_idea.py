#https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    nm = input().split()
    arr = input().split()
    _A = set(input().split())
    _B = set(input().split())

    happiness_count = 0

    for i in range(len(arr)):
        if _A.__contains__(arr[i]):
            happiness_count += 1

        if _B.__contains__(arr[i]):
            happiness_count -= 1

    print(happiness_count)
