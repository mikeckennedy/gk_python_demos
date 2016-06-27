

def run(x, y, *args):
    print("x = {}, y= {}, args= {}".format(
        x, y, args
    ))

run(1, 2, 3, 4, 5)
l = [3, 4, 5]
run(1, 2, *l)


def named(x, y="y", z="z", **kwargs):
    print(x, y, z, kwargs)


named(1, z="Last", cat=11, dog=True)
data = {'cat': True, 'dog': "Bark", 'z': 20}
named(1, **data)