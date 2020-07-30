#https://www.hackerrank.com/challenges/any-or-all/problem

def is_palindrome(num):
    actual = num
    reverse = 0
    while num != 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num //= 10
    if actual == reverse:
        return True
    else:
        return False


def all_pos(nums):
    res = []
    for i in range(len(nums)):
        res.append(nums[i] > 0)
    return all(res)

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    if all_pos(nums):
        result = []
        for i in range(n):
            result.append(is_palindrome(nums[i]))
        print(any(result))
    else:
        print(False)