#https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    def _attr_printer(self, attrs):
        if attrs:
            for attr in attrs:
                print("-> " + attr[0] + " > " + str(attr[1]) )

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self._attr_printer(attrs)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self._attr_printer(attrs)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(''.join([input().strip() for _ in range(int(input()))]))