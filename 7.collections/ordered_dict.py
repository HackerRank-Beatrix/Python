#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())

    commodities = OrderedDict()

    for i in range(n):
        commodity = input().split()
        name = ' '.join(commodity[0: len(commodity) - 1])
        price = int(commodity[len(commodity) - 1])

        if name not in commodities:
            commodities[name] = price
        else:
            commodities[name] += price

    for name, price in commodities.items():
        print(name, price)
