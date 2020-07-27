#https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(string, k):
    # your code goes here
     result = get_result_as_list(string, k)
     for i in range(len(result)):
        print(''.join(result[i]))

def get_result_as_list(string, k):
    result = []
    for i in range(int(len(string)/k)):
        str = string[(i*k) : ((i*k) + k)]
        lst = []
        for j in range(len(str)):
            if str[j] not in lst:
                lst.append(str[j])
        result.append(lst)
    return result

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)