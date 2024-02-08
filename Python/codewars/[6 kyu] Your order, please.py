'''https://www.codewars.com/kata/55c45be3b2079eccff00010f'''

import re
def order(sentence):
    if sentence is "":
        return ""
    l=sentence.split(" ")
    l.sort(key=sort_f)
    return " ".join(l)

def sort_f(x):
    return int(x[re.search(r'[0-9]+',x).start():re.search(r'[0-9]+',x).end()])
