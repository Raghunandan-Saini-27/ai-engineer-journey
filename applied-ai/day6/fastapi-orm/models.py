from sqlalchemy import Column,Integer,String
from database import engine
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class Product(Base):
	__tablename__="products"
	id=Column(Integer,primary_key=True)
	name=Column(String)
	price=Column(Integer)
	
Base.metadata.create_all(engine)