import datetime
import sqlalchemy

__table_metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    __table_metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('email', sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column('password_hash', sqlalchemy.String),
    sqlalchemy.Column('registered', sqlalchemy.DateTime, default=datetime.datetime.now)
)

addresses = sqlalchemy.Table(
    'addresses',
    __table_metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, index=True),
    sqlalchemy.Column('street_address', sqlalchemy.String)
)

def create_all(engine):
    __table_metadata.create_all(engine)
    print()
    print(repr(users))
    print()

