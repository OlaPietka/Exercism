def decode(string):
    out = ""
    repeat = ""
    for (i, c) in enumerate(string):
        if c.isdigit():
            repeat += c
        else:
            out += string[i] * (int(repeat)) if repeat is not '' else string[i]
            repeat = ""
    return out


def encode(string):
    strip = lambda x: str(count) + string[x-1] if count > 1 else string[x-1]

    out = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] is string[i-1]:
            count += 1
        else:
            out += strip(i)
            count = 1

    if out is not '':
        out += strip(len(string))
    return out
