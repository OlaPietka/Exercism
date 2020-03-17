from math import sqrt, ceil


def cipher_text(plain_text):
    if not plain_text:
        return ''

    cleaned = ''.join(filter(str.isalnum, plain_text.lower()))
    cols = ceil(sqrt(len(cleaned)))

    out = ' '.join([cleaned[c::cols] for c in range(cols)])

    if '.' in plain_text:
        return out + ' '
    return out
