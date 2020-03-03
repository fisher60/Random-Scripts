import random


class Car:
    def __init__(self):
        self.make = ''.join([chr(random.randint(97, 122)) for x in range(4)])
        self.model = (''.join([chr(random.randint(97, 122)) for x in range(random.randint(2, 100))]), ''.join([chr(random.randint(97, 122)) for x in range(random.randint(2, 100))]))
        self.year = random.randint(1886, 2020)
        self.new = random.choice([True, False])

    def to_list(self):
        final = list(self.__dict__.values())
        random.shuffle(final)
        return final


test_list1 = [1998, 'ford', ('mustang', 'gt'), False]
test_list2 = ['benz', ('motorwagen', 'basic'), False, 1886]
test_list3 = [('camry', 'basic'), True, 2020, 'toyo']


def make_model_year(lst):
    for each in lst:
        tp = type(each)
        if tp == int:
            year = each
        elif tp == str:
            make = each
        elif tp == bool:
            new = each
        else:
            model = ' '.join(each)
    return {'make': make, 'model': model, 'year': year, 'new': new}


car = Car().to_list()

print(car)
# print(make_model_year(car))
