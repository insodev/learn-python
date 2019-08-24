class Employee:
    def __new__(cls, *args, **kwargs):
        print(cls, (args, kwargs))
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('__init__', (args, kwargs))


e = Employee(12, 13)



