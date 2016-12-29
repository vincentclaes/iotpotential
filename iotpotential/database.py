# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# engine = create_engine('sqlite:////tmp/test2.db', convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()
#
# def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
#     from iotpotential import models
#     Base.metadata.create_all(bind=engine)


#########################
#    POSTGRES AWS RDS   #
#########################

import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def connect(user='potential001', password='1saJocVin$', db= 'potential001', host='potential001.ce0fcmlyqlgf.eu-central-1.rds.amazonaws.com', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    conn_string = 'host= dbname='
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    engine = sqlalchemy.create_engine(url, client_encoding='utf8')
    # We then bind the connection to MetaData()
    db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
    # meta = sqlalchemy.MetaData(bind=engine, reflect=True)

    return engine, db_session

engine, db_session = connect()

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from iotpotential.models import models
    Base.metadata.create_all(bind=engine)
