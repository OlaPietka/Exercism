from string import ascii_lowercase as low
from string import ascii_uppercase as upp


def rotate(text, key):
    return ''.join([low[(low.index(c)+key) % 26] if c.islower()
                    else upp[(upp.index(c)+key) % 26] if c.isupper()
                    else c for c in text])
