import sqlalchemy
import os
import models

db_file = os.path.join(os.path.dirname(__file__), "the_db.sqlite")
engine = sqlalchemy.create_engine("sqlite:///" + db_file, echo=True)

def create_and_update_db():
    models.create_all(engine)

def add_test_data():

    rows = engine.execute(models.users.select())
    if sum(1 for _ in rows):
        print("Data already loaded.")
        return


    engine.execute(models.users.insert(), [
        {'email': 'j@j.com', 'password_hash': "932798237498239847"},
        {'email': 'u@u.com', 'password_hash': "39084983498398"},
        {'email': 'z@google.com', 'password_hash': "01820975732"},
    ])

def find_user_by_email(email):
    rows = engine.execute(models.users.select().
                          where(models.users.c.email == email))

    return list(rows)[0]
