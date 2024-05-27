from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///pizzeriaDBase.db')
Base = declarative_base()


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    order_description = Column(String)
    date = Column(String)

    def __init__(self, name, price, order_description, date):
        self.name = name
        self.price = price
        self.order_description = order_description
        self.date = date


Base.metadata.create_all(engine)
