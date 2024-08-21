import random
import uuid

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from create_tables import FullName, ShortName


engine = create_engine('postgresql://postgres:postgres@localhost:5432/test')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


formats = ["jpeg", "png", "mp3", "mp4", "wav", "pdf", ".ppt", "mkv", "mpeg", "txt", "zip", "epub"]

short_names = []
full_names = []

for i in range(700):
    name_file = str(uuid.uuid1())
    short_names.append(ShortName(name=name_file, status=random.randint(0, 1)))

    if i < 500:
        full_names.append(FullName(name=f'{name_file}.{random.choice(formats)}'))

session.add_all(short_names)
session.add_all(full_names)
session.commit()
