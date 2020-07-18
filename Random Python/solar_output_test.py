def solution(xs):
    if xs.count(0) == len(xs) - 1 or len(xs) == 1 or len(xs) == 2 and 0 in xs:
        return str(max(xs))
    if len(xs) < 1:
        return '0'

    max_product = 1
    max_neg = -1001

    for x in xs:
        max_product = max(max_product, max_product*x, key=abs)
        if x <= -1:
            max_neg = max(x, max_neg)
    return str(max(max_product, max_product // max_neg))


print(solution([-1, 0, 0]))
