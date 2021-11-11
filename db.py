from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///productos.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

#  se le pasa la cadena de conexión a la base de datos. En este caso,
#  la cadena de conexión a la base de datos Sqlite es 
# 'sqlite:///productos.sqlite'

# Al crear un engine con la función create_engine(), se genera un pool QueuePool 
# que viene configurado como un pool de 5 conexiones como máximo. Esto se puede
# modificar en la configuración de SQLAlchemy.

#  Al crear un engine con la función create_engine(), se genera un pool QueuePool
# que viene configurado como un poolde 5 conexiones como máximo.
#  Esto se puede modificar en la configuración de SQLAlchemy.

# FUENTE:
# https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/