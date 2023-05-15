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