def factors(value):
    prime_factors, factor = [], 2

    while value > 1:
        while value % factor == 0:
            prime_factors.append(factor)
            value /= factor
        factor += 1

    return prime_factors
