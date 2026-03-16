import requests
from bs4 import BeautifulSoup
import pandas as pd

books_data=[]
for i in range(1,4):
	url=f"https://books.toscrape.com/catalogue/page-{i}.html"
	print(url)
	responses=requests.get(url)
	soup=BeautifulSoup(responses.text,"html.parser")

	item=soup.find("div",class_="col-sm-8 col-md-9")
	books=item.find_all("article",class_="product_pod")
	for book in books:
		title = book.h3.a["title"]
		price=book.find("p",class_="price_color").text
		books_data.append(
			{
				"Book Title":title,
				"Price":price
			}
		)
		print(f"Book : {title} | Price : {price}")

df=pd.DataFrame(books_data)
df.to_csv("books_multipage.csv",index=False)