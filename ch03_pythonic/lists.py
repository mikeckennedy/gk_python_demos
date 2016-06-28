import datetime

s = ['jeff', 'ted', 'robert', 'sarah']

lengths = []
for n in s:
    lengths.append(len(n))

print(lengths)

lengths2 = [
    len(name)
    for name in s
    if len(name) > 3
    ]

print(lengths2)
print([len(m) for m in s])

lengths3 = (
    len(name)
    for name in s
    if len(name) > 3
)
# print(type(lengths3))
for i in lengths3:
    print(i, end=',')
import math
import sys
print("About to compute")
sys.stdout.flush()
t0 = datetime.datetime.now()
sr = (
    math.sqrt(x)
    for x in range(0, 1000000)
    if x % 2 == 0
)

srset = {
    math.sqrt(x)
    for x in range(0, 10)
    if x % 2 == 0
}

srdict = {
    x: math.sqrt(x)
    for x in range(0, 10)
    if x % 2 == 0
}
print(srset)
print(srdict)


def sr_method():
    for x in range(0, 1000):
        if x % 2 == 0:
            yield math.sqrt(x)

# len(sr)
# c = sum(1 for _ in sr)
# print("Count = {}".format(c))

t1 = datetime.datetime.now()
dt = t1 - t0
for x in sr:
    print(x)
    if x > 10:
        break
print("Done in {} sec".format(dt.total_seconds()))