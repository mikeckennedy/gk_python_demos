import os

from db import Database
from models import User


def list_user():
    email = 'ted@gmail.com'
    user = find_user(email)
    print("Looking at user ID")
    print("Found user: {}".format(user.id))


def find_user(email):
    # email = input("Enter your email: ")

    session = Database.create_session()
    session.expire_on_commit = False
    # with Database.create_session() as session:

    user = session.query(User). \
        filter(User.email == email).\
        order_by(User.registered.desc())


    user = user.first()
    if user:
        # print("results: {}".format(user.name))
        user.name = user.name.upper()
        session.commit()
        print("Saved user")
        session.close()
        return user
    else:
        # print("not found!")
        return None

def page_of_users():
    # email = input("Enter your email: ")

    session = Database.create_session()
    session.expire_on_commit = False
    # with Database.create_session() as session:

    users = session.query(User). \
        filter(User.id != None).\
        order_by(User.registered.desc())

    page_size = 10
    current_page = 3

    results = users[page_size * current_page:page_size * (current_page+1)]
    # results = users[1:5]

    for u in results:
        print(u.name)

def main():
    init_db()
    add_data()
    list_user()
    page_of_users()


def init_db():
    dbfile = os.path.join(os.path.dirname(__file__), 'db.sqlite')
    Database.global_init(dbfile)


def add_data():
    session = Database.create_session()

    num = session.query(User).count()
    if num:
        print("data loaded, skipping")
        return

    u = User(
        name='Michael',
        email='mikeckennedy@gmail.com',
        pw='a'
    )
    session.add(u)

    u = User(
        name='Ted',
        email='ted@gmail.com',
        pw='9837598w75983749857349857398745'
    )
    session.add(u)
    session.commit()


if __name__ == '__main__':
    main()
