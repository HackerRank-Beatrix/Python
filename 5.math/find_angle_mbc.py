#https://www.hackerrank.com/challenges/find-angle/problem

from math import atan2, degrees

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

    print(str(round(degrees(atan2(AB, BC)))) + '°')
