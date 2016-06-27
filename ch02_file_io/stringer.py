import json


class Stringer:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __str__(self):
        return "A = {} and B = {}".format(self.a, self.b)

    def __repr__(self):
        d= self.__dict__.copy()
        d['type'] = 'Stringer'
        return json.dumps(d)

s = Stringer()
print(s)
data = [s, s, s]
print(data)
