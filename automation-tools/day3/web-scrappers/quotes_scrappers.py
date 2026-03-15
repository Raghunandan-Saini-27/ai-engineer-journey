import requests
from bs4 import BeautifulSoup
import pandas as pd

url="http://quotes.toscrape.com"

response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
items=soup.find_all('div',class_='quote')
all_quotes = []

for item in items:
	text=item.find('span',class_='text').text
	author=item.find('small',class_='author').text
	all_quotes.append({"Quote": text, "Author": author})
	print(f'{text}-{author}')

# Create a DataFrame and save it
df = pd.DataFrame(all_quotes)
df.to_csv("quotes.csv", index=False)