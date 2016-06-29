import db

def main():
    print("Creating or updated db...", end='')
    db.create_and_update_db()
    print(" done.")

    print("Adding fake data...", end='')
    db.add_test_data()
    print(" done.")

    user = db.find_user_by_email('j@j.com')
    print(user)

if __name__ == '__main__':
    main()