from math import factorial


def combos(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


print(combos(60, 16))
