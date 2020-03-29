def largest(min_factor, max_factor):
    return palindrome_number(min_factor, max_factor, max)


def smallest(min_factor, max_factor):
    return palindrome_number(min_factor, max_factor, min)


def palindrome_number(mn, mx, func):
    if mn > mx:
        raise ValueError("Min is more then max")

    products = palindrome_products(mn, mx)

    if not products:
        return None, []

    number = func(products)
    return number, factors(mn, mx, number)


def palindrome_products(mn, mx):
    return [i*j for i in range(mn, mx+1) for j in range(i, mx+1) if is_palindrome(i*j)]


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def factors(mn, mx, value):
    return [[i, j] for i in range(mn, mx+1) for j in range(i, mx+1) if i * j == value]
