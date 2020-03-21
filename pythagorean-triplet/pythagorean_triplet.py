def triplets_with_sum(n):
    return [[a, b, n - a - b] for a in range(n//3) for b in range(a+1, n//2) if is_triplet(a, b, n - a - b)]


def is_triplet(a, b, c):
    return a**2 + b**2 == c**2
