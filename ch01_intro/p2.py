def main():
    print_header()
    name = get_user_name()
    print("Hello {}".format(name))


def print_header():
    print("--------------------------------")
    print("     THE MAIN APP ")
    print("--------------------------------")


def get_user_name():
    return input("What is your name? ")

if __name__ == '__main__':
    main()
