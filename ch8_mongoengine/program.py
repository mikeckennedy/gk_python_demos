import data

def main():
    # needs to run first
    data.setup_db()

    data.add_some_data()
    data.run_query()


if __name__ == '__main__':
    main()