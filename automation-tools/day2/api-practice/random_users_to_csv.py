import requests
import pandas as pd
from datetime import datetime

url="https://randomuser.me/api/?results=5"
response=requests.get(url)
raw_data=[]
	
data=response.json()
for user in data["results"]:								#Fetch users
	name=user["name"]["first"]+" "+user["name"]["last"]		#---	
	email=user["email"]										#--|-->Extract Data
	country=user["location"]["country"]						#---
	print("Name : ",name)
	print("Email : ",email)
	print("Country : ",country)
	print("-"*20)
	raw_data.append({"name":name,"email":email,"country":country,
				  "timestamp":datetime.utcnow()})

df=pd.DataFrame(raw_data)
df.to_csv("day2/users.csv",index=False)						#Save into CSV
