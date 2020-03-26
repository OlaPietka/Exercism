def classify(number):
    if number <= 0:
        raise ValueError(str(number) + " is not natural number")

    aliquot_sum = sum(factors(number))

    return (("perfect", "abundant")[aliquot_sum > number], "deficient")[aliquot_sum < number]


def factors(number):
    return [n for n in range(1, number) if number % n == 0]
