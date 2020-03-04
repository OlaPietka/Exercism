import string


def response(hey_bob):
    hey_bob = hey_bob.translate({ord(c): None for c in string.whitespace})

    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif hey_bob is "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
