def primes(limit):
    numbers = set(range(2, limit + 1))
    marked = {m for n in numbers for m in range(2 * n, limit + 1, n)}
    return sorted(numbers - marked)
