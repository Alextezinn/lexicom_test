from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:postgres@localhost:5432/test')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class ShortName(Base):
    __tablename__ = 'short_names'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    status = Column(String)

class FullName(Base):
    __tablename__ = 'full_names'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    status = Column(String, )

# Создание таблиц
Base.metadata.create_all(engine)