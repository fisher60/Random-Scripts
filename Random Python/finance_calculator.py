from os import system


def get_name():
    return input("type the name here:\n")


def get_frequency():
    options = {
        1: 'monthly',
        2: 'weekly',
        3: 'daily',
        4: 'yearly'
    }
    rendered_options = '\n'.join([f'{k}: {v}' for k, v in options.items()])

    try:
        this_answer = int(input(f'Select One \n{rendered_options}'))
    except ValueError:
        print("Please enter a valid type")
        return get_frequency()

    if this_answer in options:
        return options[this_answer]
    else:
        print("Please enter a valid type")
        return get_frequency()


def get_amount():
    try:
        this_amount = float(input("Specify the amount"))
    except ValueError:
        print("Please enter a number")
        return get_amount()
    if this_amount < 0:
        this_amount *= -1

    return this_amount


def clear():
    return system('cls')


class Finances:
    gross_monthly_income = 0
    gross_monthly_expenses = 0
    net_income = 0
    incomes = []
    expenses = []

    def __str__(self):
        return f'Net income is: {self.calc_monthly_net()}'

    def collect_gross_expenses(self):
        for expense in self.expenses:
            if expense.frequency == 'yearly':
                modifier = 12
            elif expense.frequency == 'monthly':
                modifier = 1
            elif expense.frequency == 'weekly':
                modifier = 0.25
            elif expense.frequency == 'daily':
                modifier = 0.03333
            else:
                raise ValueError("frequency does not match any option")

            print(f'modifier {modifier}')

            self.gross_monthly_expenses = expense.amount/modifier
            return self.gross_monthly_expenses

    def collect_gross_incomes(self):
        for income in self.incomes:
            if income.frequency == 'yearly':
                modifier = 12
            elif income.frequency == 'monthly':
                modifier = 1
            elif income.frequency == 'weekly':
                modifier = 0.25
            else:
                modifier = 0.03333

            print(f'modifier {modifier}')

            self.gross_monthly_income = income.amount/modifier
            return self.gross_monthly_income

    def calc_monthly_net(self):
        self.net_income = sum([self.gross_monthly_income, self.gross_monthly_expenses])
        return self.net_income


class Expense:
    def __init__(self):
        self.name = get_name()
        clear()
        self.frequency = get_frequency()
        clear()
        self.amount = get_amount() * -1
        clear()


class Income:
    def __init__(self):
        self.name = get_name()
        clear()
        self.frequency = get_frequency()
        clear()
        self.amount = get_amount()
        clear()


this_finance = Finances()
this_finance.incomes.append(Income())
this_finance.expenses.append(Expense())

this_finance.collect_gross_expenses()
this_finance.collect_gross_incomes()

print(this_finance)
