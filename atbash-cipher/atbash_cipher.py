from string import ascii_lowercase as low


def get_reversed(char):
    return list(reversed(low))[low.index(char)] if char in low else char


def encode(plain_text):
    plain_text = ''.join(c.lower() for c in plain_text if c.isalnum())
    rev_text = ''.join([get_reversed(char) for char in plain_text])
    return ' '.join(rev_text[i:i+5] for i in range(0, len(rev_text), 5))


def decode(ciphered_text):
    return ''.join([get_reversed(char) for char in ciphered_text.replace(' ', '')])
