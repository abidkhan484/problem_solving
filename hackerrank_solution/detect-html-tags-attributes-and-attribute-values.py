from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print('->', i[0], '>', i[1])

string = ''
for _ in range(int(input().strip())):
    string += input()+'\n'

parser = MyHTMLParser()
parser.feed(string)
parser.close()
