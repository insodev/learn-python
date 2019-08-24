# z = {}
# z.setdefault('f', [])
# print(z)
#
# z['f'].append('a')
# z.setdefault('f', [])
# print(z)

class A:
    def __call__(self, *args, **kwargs):
        print(args, kwargs)


A()()
