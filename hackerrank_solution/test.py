Regex_Pattern = r'(\w)(?!\1)'


import re

Test_String = 'gooooo'

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
