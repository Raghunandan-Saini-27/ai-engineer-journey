from fastapi import FastAPI
from pydantic import BaseModel
from database import engine,SessionLocal
from models import Base,Product 
from typing import List

app=FastAPI()
class ProductCreate(BaseModel):
	name:str
	price:int

@app.get("/")
def home():
	return {"message":"API workking sucessfully."}

@app.post("/add-product")
def add_product(data:ProductCreate):
	session=SessionLocal()
	new_product=Product(name=data.name,price=data.price)
	session.add(new_product)
	session.commit()
	session.refresh(new_product)
	session.close()
	return {"message":f"{data.name} is added to the database successfully."}

@app.get("/products")
def get_products():
	session=SessionLocal()
	all_products=session.query(Product).all()
	session.close()
	return all_products