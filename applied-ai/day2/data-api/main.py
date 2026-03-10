import pandas as pd
from fastapi import FastAPI

app=FastAPI()
df=pd.read_csv("data/products.csv")
df["revenue"]=df["price"]*df["quantity"]
df.to_csv("data/products.csv",index=False)

@app.get("/")
def home():
	return {"message":"API working sucessfuly."}

@app.get("/products")								#Endpoint 1 — Get All Products
def products():
	return df.to_dict(orient='records')

@app.get("/revenue")								#Endpoint 2 — Revenue
def revenue():
	total_revenue=df["revenue"].sum()
	return {"Total revenue ":float(total_revenue)}

@app.get("/products/{product_name}")				#Endpoint 3 — Product Search
def product_name(product_name:str):
	product_data=df[df["product"]==product_name]
	if product_data.empty:
		return {"error":"Product not found"},404
	
	return product_data.iloc[0].to_dict()