def prime(number):
    if number is 0:
        raise ValueError("Error")
    return n_primes(n=number)[-1]


def n_primes(n):
    primes = [2]
    number = 3

    while len(primes) < n:
        for p in primes:
            if number % p == 0:
                break
        else:
            primes.append(number)
        number += 2
    return primes
