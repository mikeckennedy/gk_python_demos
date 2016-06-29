import sqlalchemy
import sqlalchemy.orm
import models


class Database:
    __engine = None
    __conn_string = None
    __session_factory = None

    @staticmethod
    def global_init(db_file):
        Database.__conn_string = "sqlite:///" + db_file
        Database.__engine = sqlalchemy.create_engine(Database.__conn_string, echo=True)
        models.SqlAlchemyBase.metadata.create_all(Database.__engine)
        Database.__session_factory = sqlalchemy.orm.sessionmaker(bind=Database.__engine)

    @staticmethod
    def create_session():
        return Database.__session_factory()
