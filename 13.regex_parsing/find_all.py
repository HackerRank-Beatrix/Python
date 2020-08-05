#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
import re

if __name__ == '__main__':
    VOWELS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    REGEX = '(?<=[' + CONSONANTS + '])([' + VOWELS + ']{2,})[' + CONSONANTS + ']'

    match = re.findall(REGEX, input(), re.IGNORECASE)
    if match:
        print(*match, sep='\n')
    else:
        print('-1')