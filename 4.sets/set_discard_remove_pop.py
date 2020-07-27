#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))

nc = int(input())

for i in range(nc):
    c, *valarr = input().split()
    val = None
    if valarr != []:
        val = int(valarr[0])
    if c == 'pop':
        s.pop()
    elif c == 'remove':
        s.remove(val)
    elif c == 'discard':
        s.discard(val)
    else:
        raise ValueError('Invalid command')

print(sum(s))
