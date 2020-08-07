#https://www.hackerrank.com/challenges/html-parser-part-2/problem

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        num_of_lines = len(data.split('\n'))
        if num_of_lines <= 1:
            print('>>> Single-line Comment')
        else:
            print('>>> Multi-line Comment')

        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print('>>> Data')
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()