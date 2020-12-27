def wrapper(f):
    def fun(l):
        # complete the function
        # result = []
        # for n in l:
        #     if len(n) == 11:
        #         result.append("+91 " + n[1:6] + " " + n[6:])
        #     elif(len(n) == 13):
        #         result.append("+91 " + n[3:8] + " " + n[8:])
        #     elif(len(n) == 12):
        #         result.append("+91 " + n[2:7] + " " + n[7:])
        #     else:
        #         result.append("+91 " + n[0:5] + " " + n[5:])
        # f(result)
        f("+91 " + p[-10:-5] + " " + p[-5:] for p in l)
    return fun

@wrapper
def sort_phone(l):
    print('\n'.join(sorted(l)))

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)