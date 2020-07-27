#https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result = []
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                result.append(s[i].upper())
            else:
                result.append(s[i].lower())
        else:
            result.append(s[i])

    return ''.join(result)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)