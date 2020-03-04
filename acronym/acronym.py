import re

def abbreviate(words):
    return ''.join([word[0] for word in re.findall("(?:[0-9]+|[A-Z]+(?:'[A-Z])?)", words.upper())])