
def find_special_nums(test, limit):
    for n in range(0, limit):
        if test(n):
            print(n, end=', ')

def is_even(num):
    return num % 2 == 0

print(is_even)
print()

find_special_nums(is_even, 7)
print()
find_special_nums(lambda x: x % 11 == 1 , 70)
