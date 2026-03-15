import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://books.toscrape.com"
responses=requests.get(url)
soup=BeautifulSoup(responses.text,"html.parser")

items=soup.find("div",class_="col-sm-8 col-md-9")
books=items.find_all("article",class_="product_pod")
books_list=[]

for book in books:
	title = book.h3.a["title"]
	price=book.find("p",class_="price_color").text
	books_list.append(
		{
			"Book Title":title,
			"Price":price
		}
	)
	print(f"Book : {title} | Price : {price}")

df=pd.DataFrame(books_list)
df.to_csv("books.csv",index=False)