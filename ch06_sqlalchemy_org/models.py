import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sql

# one per DB
SqlAlchemyBase = declarative_base()


class User(SqlAlchemyBase):
    __tablename__ = 'User'

    # id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    id = sql.Column(sql.String, primary_key=True,
                    default=lambda: str(uuid.uuid4()).replace('-', '')[:12])
    name = sql.Column(sql.String, nullable=False)
    email = sql.Column(sql.String, nullable=False, index=True, unique=True)
    pw = sql.Column(sql.String)
    registered = sql.Column(sql.DateTime, default=datetime.datetime.now)


class Address(SqlAlchemyBase):
    __tablename__ = 'Address'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    user_id = sql.Column(sql.Integer)


