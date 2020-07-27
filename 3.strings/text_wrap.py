#https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    result = ""
    num_of_lines = (len(string)//max_width) + 1
    if num_of_lines == 0:
        result = string
    else:
        for i in range(0, len(string), max_width):
            result = result + string[i: i+max_width]
            result += "\n"
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)