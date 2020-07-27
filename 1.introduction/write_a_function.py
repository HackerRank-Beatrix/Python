import calendar
#https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    return calendar.isleap(year)


year = int(input())
print(is_leap(year))