import collections

Reading = collections.namedtuple("Reading", "y x z value")

def get_data():
    return [
        (1.2, 3.2, 5, 45),
        (1.5, 3.7, 5, 46),
        (1.9, 4.1, 5, 51),
    ]

def get_data2():
    return [
        Reading(1.2, 3.2, 5, 45),
        Reading(1.5, 3.7, 5, 46),
        Reading(1.9, 4.1, 5, 51),
    ]
