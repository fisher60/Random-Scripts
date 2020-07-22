def solution(x, y):
    x = int(x)
    y = int(y)
    final = 0

    while not (x == 1 and y == 1):
        print((x, y))
        if x <= 0 or y <= 0:
            return 'impossible'
        if y == 1:
            return str(final + x - 1)
        else:
            final += x//y
            x, y = y, x % y

    return str(final)


print(solution('4', '7'))