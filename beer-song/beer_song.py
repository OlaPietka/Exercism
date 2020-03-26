def recite(start, take=1):
    out = []

    for i in range(take):
        for v in verse(start-i):
            out.append(v)
        out.append("")
    return out[:-1]


def verse(n):
    if n is 0:
        return ["No more bottles of beer on the wall, no more bottles of beer.",
                "Go to the store and buy some more, 99 bottles of beer on the wall."]
    if n is 1:
        return ["1 bottle of beer on the wall, 1 bottle of beer.",
                "Take it down and pass it around, no more bottles of beer on the wall."]
    if n is 2:
        return ["2 bottles of beer on the wall, 2 bottles of beer.",
                "Take one down and pass it around, 1 bottle of beer on the wall."]
    else:
        return ["{num} bottles of beer on the wall, {num} bottles of beer.".format(num=n),
                "Take one down and pass it around, {num} bottles of beer on the wall.".format(num=n-1)]
