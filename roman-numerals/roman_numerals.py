roman_conv = {
    1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"
}


def roman(number):
    out = ""

    for (i, n) in enumerate(str(number), 1):
        zeros = 10 ** (len(str(number)) - i)
        n = int(n)

        if n in [1, 2, 3]:
            out += roman_conv[zeros] * n
        elif n in [5, 6, 7, 8]:
            out += roman_conv[5 * zeros] + roman_conv[zeros] * (n - 5)
        elif n in [4, 9]:
            out += roman_conv[zeros] + roman_conv[zeros * 10 / (10 // n)]
    return out
