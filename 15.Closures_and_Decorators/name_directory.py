import operator

def person_lister(f):
    def inner(people):
        # complete the function
        result = sorted(people, key=lambda p: int(p[2]))
        result = [f(r) for r in result]
        return result
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')