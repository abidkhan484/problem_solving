from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        if attrs:
            for i in attrs:
                print('->', i[0], '>', i[1])
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        if attrs:
            for i in attrs:
                # this join method i just got from the editorial
                print(('->', ' > ').join(map(str,attrs)))

string = ''
for _ in range(int(input().strip())):
    string += input()

parser = MyHTMLParser()
parser.feed(string)
parser.close()

'''
import re

string = '<html><head><title>HTML Parser - I</title></head>\
<body data-modal-target class=\'1\'><h1>HackerRank</h1><br /></body></html>'

startTag = r'<.+>'
li = re.findall(startTag, string)
print(li)
'''
