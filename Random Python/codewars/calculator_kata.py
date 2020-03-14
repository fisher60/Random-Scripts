class Calculator(object):
    def __init__(self):
        self.symbols = {'+': add, '-': subtract, '*': mult, '/': div}

    def evaluate(self, string):
        if "*" in string or "/" in string or "+" in string or "-" in string:
            self.to_eval = string.split(' ')
            self.calc(['*', '/'])
            self.calc(['+', '-'])
        else:
            return int(string)

        return self.to_eval[0]

    def calc(self, operators):
        index = 1
        while index < len(self.to_eval) - 1:
            if self.to_eval[index] in operators:
                solved_expression = self.symbols[self.to_eval[index]](float(self.to_eval[index - 1]), float(self.to_eval[index + 1]))
                self.to_eval[index - 1] = solved_expression
                self.to_eval.pop(index + 1)
                self.to_eval.pop(index)
                continue
            index += 1


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


print(8 == Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))