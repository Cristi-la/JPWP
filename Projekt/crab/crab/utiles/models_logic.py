from datetime import datetime, timezone
from sqlalchemy import Column, Integer, DateTime, inspect
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from crab.cli.templates.settings import DATABASE

if DATABASE['user']['ip'] == '' or DATABASE['username']['ip'] == '' or DATABASE['password']['ip'] == '' or DATABASE['engine']['ip'] == '':
    url = DATABASE['local']['engine'] + DATABASE['local']['database_name']
else:
    url = DATABASE['user']['engine'] + DATABASE['user']['username'] + DATABASE['user']['password'] + DATABASE['user']['ip']

Base = declarative_base()
db_engine = create_engine(url)
db_session = sessionmaker(bind=db_engine)

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), nullable=True)

    @classmethod
    def create(cls):
        inspector = inspect(db_engine)
        if not inspector.has_table(cls.__name__):
            cls.__table__.create(db_engine)

    def save(self, commit=True):
        session = db_session()
        session.add(self)

        if commit:
            try:
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

        session.close()

    def update(self):
        session = db_session()
        session.commit()
        session.close()

    def delete(self, commit=True):
        session = db_session()
        session.delete(self)

        if commit:
            session.commit()

        session.close()

    @classmethod
    def delete_id(cls, id, commit=True):
        session = db_session()
        instance = session.query(cls).filter_by(id=id).first()

        if instance:
            session.delete(instance)
            if commit:
                session.commit()

        session.close()

    @classmethod
    def pop(cls, commit=True):
        session = db_session()
        last_instance = session.query(cls).order_by(cls.id.desc()).first()

        if last_instance:
            session.delete(last_instance)
            if commit:
                session.commit()

        session.close()

    @classmethod
    def read(cls):
        session = db_session()
        instance = session.query(cls).all()
        session.close()
        return instance

    @classmethod
    def read_id(cls, id):
        session = db_session()
        instance = session.query(cls).filter_by(id=id).first()
        session.close()
        return instance

    @classmethod
    def clear(cls):
        session = db_session()
        count = session.query(cls).count()

        for i in range(count):
            cls.pop()

        session.close()

    @classmethod
    def bulk_create(cls, iterable, **kwargs):
        session = db_session()
        model_objs = []

        for data in iterable:
            if not isinstance(data, cls):
                data = cls(**data)

            model_objs.append(data)

        session.bulk_save_objects(model_objs)

        if kwargs.get('commit', True) is True:
            session.commit()

        session.close()
        return model_objs