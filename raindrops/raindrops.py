def convert(number):
    string = ''
    if number % 3 is 0:
        string += "Pling"
    if number % 5 is 0:
        string += "Plang"
    if number % 7 is 0:
        string += "Plong"
    return string if string is not '' else str(number)
