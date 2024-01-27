'''https://www.codewars.com/kata/54b724efac3d5402db00065e'''

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    str=[]
    words=morse_code.strip().split("   ")
    for word in words:
        l=[]
        letters = word.split(" ")
        for letter in letters:
            l.append(MORSE_CODE[letter])
        l.append(" ")
        str.append("".join(l))
    return "".join(str).strip()
