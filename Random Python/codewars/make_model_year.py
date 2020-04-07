import random



class Car:
    def __init__(self):
        self.make = ''.join([chr(random.randint(97, 122)) for x in range(4)])
        self.model = (''.join([chr(random.randint(97, 122)) for x in range(random.randint(2, 100))]),
                      ''.join([chr(random.randint(97, 122)) for x in range(random.randint(2, 100))]))
        self.year = random.randint(1886, 2020)
        self.new = random.choice([True, False])

    def to_list(self):
        final = list(self.__dict__.values())
        random.shuffle(final)
        return final


def test_function(lst):
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


for _ in range(10**6):
    car = Car().to_list()
    this = test_function(car)
