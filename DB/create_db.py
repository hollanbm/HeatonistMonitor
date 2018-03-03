from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    url = Column(String(1000), nullable=False, primary_key=True)
    name = Column(String(250), nullable=True)
    price = Column(Integer,nullable=True)
    instock = Column(Integer, nullable=True)
    lastupdate = Column(DateTime,nullable=True)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///heatonist_monitor.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)