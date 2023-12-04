from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print(data)
        if '\n' in data:
            print('>>> Multi-line Comment\n' + data)
        else:
            print('>>> Single-line Comment\n' + data)

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data\n' + data)
        

string = ''
for _ in range(int(input().strip())):
    string += input().rstrip()+'\n'

parser = MyHTMLParser()
parser.feed(string)
parser.close()
