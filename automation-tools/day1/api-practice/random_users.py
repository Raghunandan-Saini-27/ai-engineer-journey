import requests

url="https://randomuser.me/api/?results=5"

response=requests.get(url)

if response.status_code == 200:
    print("Request successful")
else:
    print("API failed")
    
data=response.json()

for user in data["results"]:
	name=user["name"]["first"]+" "+user["name"]["last"]
	email=user["email"]
	country=user["location"]["country"]

	print("Name : ",name)
	print("Email : ",email)
	print("Country : ",country)
	print("-"*20)