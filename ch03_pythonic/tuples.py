from tuple_support import get_data, get_data2, Reading

# for d in get_data():
#     print('({}, {}), reading: {}'.format(
#         d[1], d[0], d[2]
#     ))

for d in get_data2():
    print('({}, {}), reading: {}'.format(
        d.x, d.y, d.value
    ))

t = (1,2,3,4)
r = Reading(*t)
print(r)