import enum
import random

class Days(enum.Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5


def get_random_day():
    days = [Days.Monday, Days.Tuesday, Days.Wednesday, Days.Thursday, Days.Friday]
    day = random.choice(days)
    return day


today = get_random_day()
print("Looks like today is {}".format(today))

# semi non pythonic
if today == Days.Monday or today == Days.Wednesday or today == Days.Friday:
    print("Your class is 50 minutes")
else:
    print("Your class is 1 hr 20 minutes")

# pythonic
if today in {Days.Monday, Days.Wednesday, Days.Friday}:
    print("Your class is 50 minutes")
else:
    print("Your class is 1 hr 20 minutes")

def append_data(item, lst = None):
    if lst is None:
        lst = []

    lst.append(item)
    return lst


data = []
append_data(42, data)
append_data(77, data)
print(data)















