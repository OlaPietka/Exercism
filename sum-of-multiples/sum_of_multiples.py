def sum_of_multiples(limit, multiples):
    return sum({n for n in range(limit) for m in multiples if m != 0 and n % m == 0})
