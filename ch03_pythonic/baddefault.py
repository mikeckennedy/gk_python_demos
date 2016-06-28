# def append_data(item, lst=[]):
#     lst.append(item)
#     return lst

def append_data(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

data = append_data(7)
append_data(11, data)
append_data(12, data)
append_data(42, data)
print(data)

data2 = append_data(70)
append_data(110, data2)
append_data(120, data2)
append_data(420, data2)
print(data2)

print(id(data), id(data2), data is data2)