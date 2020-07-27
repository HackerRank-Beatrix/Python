#https://www.hackerrank.com/challenges/text-alignment/problem

if __name__ == '__main__':
    n, m = input().split()
    n = int(n)
    m = int(m)
    DESIGN_TEXT = '.|.'
    WELCOME_TEXT = 'WELCOME'

    welcome_line = ''.join(['-' for i in range((m - 7) // 2)])
    welcome_line += WELCOME_TEXT
    welcome_line += ''.join(['-' for i in range((m - 7) // 2)])

    lines = []
    repitition_count = 1
    for i in range(n // 2):
        line = ''.join(['-' for k in range((m - (repitition_count * 3)) // 2)])
        for j in range(repitition_count):
            line += DESIGN_TEXT
        line += ''.join(['-' for k in range((m - (repitition_count * 3)) // 2)])
        # print(line)
        lines.append(line)
        repitition_count += 2

    result = ''
    for p in range(2):
        for l in range(len(lines)):
            result += ''.join(lines[l])
            result += "\n"

        if p == 0:
            result += welcome_line
        result += "\n"
        lines.reverse()

    print(result)