import re

regex = '^\s*#'
# in this problem i need to know 'positive look behind'
# and 'positive lookahead' idea. at first i wrote like this
# pattern = ' && '; pattern2 = ' \|\| '
pattern = '(?:^|(?<=\s))&&(?=\s|$)'; pattern2 = '(?:^|(?<=\s))\|\|(?=\s|$)'

for i in range(int(input().strip())):
    string = input()
    find = re.search(pattern, string)
    find2 = re.search(pattern2, string)
    if find or find2:
        if re.search(regex, string):
            print(string)
            continue
        string = re.sub(pattern, 'and', string)
        string = re.sub(pattern2, 'or', string)
    print(string)
