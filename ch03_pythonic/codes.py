import sys


def main(x, y):
    n = int(input("Enter an even number"))
    print(x, y)
    if 7:
        return True

    if n % 2 == 1:
        print("No that's not even!")
        sys.exit(-1)

    print("Great, it's 2 * {}".format(n / 2))


if __name__ == '__main__':
    main(1, 2)
