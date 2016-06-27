# try:
#     xrange = xrange
# except:
#     xrange = range

# age = int(input("How old are you?"))
#
# # age < 32 ? "You're young" : "Not so..."
# print("You're young" if age < 32 else "You're not so young")
#
# if age < 18:
#     print("Isn't it past your bedtime?")
#     print("Good night")
# elif age < 25:
#     print("See you at bar")
# else:
#     print("Time for my bedtime")
#
# name = "Michael"
# print(name, type(name))
name = [10, 20, 30]
# print(name, type(name))
#
#
# def some_method(n):  # int):
#     print("Hi there " + n)
#
#
# l = [1, 2, 4]
#
# print(id(l))
# print(id(name))
#
# print(l is name)
#
# l = name
#
# print(id(l))
# print(id(name))
#
# print(l is name)
#
# some_method("Jeff")
# print(None, id(None))
#
#
# # Loops **************************
#
# # for i=0; i<len(name); i++:
# #     print(name[i])
#
#
# for ch in name:
#     print(ch, end=', ')
# print()
#
# index = 0
# for ch in name:
#     index += 1
#     print("{0}. {1}".format(index, ch))


def some_method():
    return 1, 99, "HIGH QUALITY"


t, _, l, _ = (1, 'a', 'b', 'c')
print(t, l)

# a, b, c = *l


i, v, q = some_method()
print(i, v, q)

t2 = some_method()


#
for t in enumerate(name):
    print(type(t))
    idx, ch = t
    print("{0}. {1}".format(idx, ch))
#
#
# # bad
# index = 0
# while index < 5:
#     index += 1
#     print("{0}^2 = {1}".format(index, index**2))
#
# for n in range(6):
#     print("{0}^2 = {1}".format(n, n ** 2))


# print(xrange(100))

#
# import json
# # import passlib
# # import requests
#
# data = dict(name="michael", age=43, home_town='Portland, OR')
#
# s = json.dumps(data)
# print(s)

#
# import random
# # import data.utils.fake_data
#
# # cat_names = data.utils.fake_data.get_cat_names()
# # from data.utils.fake_data import get_cat_names
# # import data.utils.fake_data as fake
# from statistics import mean  # , median, mode
# from data.utils.fake_data import get_cat_names
#
# print(mean.__module__)
# cat_names = get_cat_names()
# # cat_names = fake.get_cat_names()
# cat_name = random.choice(cat_names)
# ml = mean([len(n) for n in cat_names])
# print("The mean length of cat names is {}".format(ml))
#
# print("My favorite cat name is {}".format(cat_name))

message = ("This is my message it is ........." +
           "...................................." +
           "...................")
print(message)

dow = "Monday"
day = 26000000

print("Today is %s the %dth" % (dow, day))
print("Today is {} the {}th".format(dow, day))
print("Today is {0} the {1}th, yeah, that's right it's {0}".format(dow, day))

print("Today is {day} the {num}th, yeah, that's right it's {day}"
      .format(day=dow, num=day))

data = {'day': "Tuesday", 'num': 27}

print("Today is {day} the {num}th, yeah, that's right it's {day}"
      .format(**data))

# python 3.6, string interpolation:
# print(f"Today is {dow} the {day}th, yeah, that's right it's {dow}")


data = [1, 1, 2, 3, 5, 8, 13, 21, 34]

print("First fib: {}".format(data[0]))
print("last fib: {}".format(data[-1]))

print("Last three: {}".format(data[len(data)-4:len(data)]))
print("Last three: {}".format(data[-4:]))
#
# query = run_db_query()
#
# print("First items {}".format(query[:5]))
# SELECT * FROM Records Limit 5 Skip 0


t = 1, 2
print(t, type(t))
