from fastapi import FastAPI
from pydantic import BaseModel
from database import create_connection,add_product_to_db,get_all_products,update_the_product,delete_the_product
class Product(BaseModel):
	name:str
	price:int
	quantity:int

app=FastAPI()

@app.on_event("startup")
def start_up():
	create_connection()

@app.get("/")
def home():
	return {"message":"API working sucessfully."}

@app.post("/add-product")
def add_product(product:Product,status_code=201):
	data=[(product.name,product.price,product.quantity)]
	add_product_to_db(data)
	return {"message" : f"Product {product.name} added sucessfully."}

@app.get("/products")
def products():
	all_products=get_all_products()
	if not all_products:
		return []
	return [dict(row) for row in all_products]

@app.put("/update-product/{product_id}")
def update_product(product_id: int,product:Product):
	data=[(product.name,product.price,product.quantity,product_id)]
	update_the_product(data)
	return {"message":f"Updated {product.name} products."}

@app.delete("/delete-product/{product_id}")
def delete_product(product_id:int):
	rows_affected=delete_the_product(product_id)
	if rows_affected==0:
		return {"message":f"{product_id} product deletion failed."}
	return {"message":f"Sucessfully deleted product {product_id}.","rows affected":rows_affected}