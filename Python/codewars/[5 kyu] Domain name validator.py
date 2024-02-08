'''https://www.codewars.com/kata/5893933e1a88084be10001a3'''

import re
def validate(domain):
    chars=re.compile('^[a-zA-Z0-9\-]*$')
    levels=domain.split(".")
    if len(domain)>253: # Domain name must not be longer than 253 characters
        return False
    if len(levels)<2 or len(levels)>127: # Domain name must not contain more than 127 levels
        return False
    for level in levels:
        if len(level)>63 or level=='': # Level names must not be longer than 63 characters
            return False
        if not chars.match(level): # Level names must be composed out of lowercase and uppercase ASCII letters, digits and - (minus sign) character
            return False
        if level.startswith('-') or level.endswith('-'): # Level names must not start or end with - (minus sign) character
            return False
    
    if re.match(r'^[0-9]*$',levels[-1]): # TLD must not be fully numerical
        return False

    return True
