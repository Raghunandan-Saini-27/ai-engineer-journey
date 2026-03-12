from fastapi import FastAPI
from pydantic import BaseModel
from database import create_connection,add_product_to_db,get_all_products,get_total_price
app=FastAPI()

class Product(BaseModel):
	name:str
	price:int 

@app.on_event("startup")
def startup():
	create_connection()

@app.get("/")
def home():
	return {"message":"API working sucessfully."}

@app.post("/add-product",status_code=201)
def add_product(product:Product):
	data=[(product.name,product.price)]
	add_product_to_db(data)
	return {"message": f"Product {product.name} added successfully!"}

@app.get("/products")
def products():
	all_products=get_all_products()
	if not all_products:
		return []
	return  [dict(row) for row in all_products]

@app.get("/total-price")
def total_price():
	total=get_total_price()
	return {"total_sum":total}