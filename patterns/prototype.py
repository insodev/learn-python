from copy import copy, deepcopy


class Prototype:
    def __init__(self, value):
        self.value = value
        self.array = [value, value, value]

    def __str__(self):
        return '%r : %s, %s' % (self, self.value, self.array)


a = Prototype(10)

b = deepcopy(a)


print(a)

b.array[0] = 20

print(b)


