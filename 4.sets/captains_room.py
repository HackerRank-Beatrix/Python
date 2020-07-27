#https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter
if __name__ == '__main__':
    k = int(input())
    roomnums = map(int, input().split())
    print(Counter(roomnums).most_common()[-1][0])
