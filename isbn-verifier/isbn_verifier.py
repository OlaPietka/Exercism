def is_valid(isbn):
    isbn = str(isbn.replace('-', ''))

    if len(isbn) != 10:
        return False

    sum = 0
    for (i, digit) in enumerate(isbn):
        if digit.isdigit():
           sum += int(digit) * (10 - i)
        elif i == 9 and digit is 'X':
            sum += 10
        else:
            return False

    return sum % 11 == 0
