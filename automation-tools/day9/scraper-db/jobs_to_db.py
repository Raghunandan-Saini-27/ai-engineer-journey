import requests 
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from database import create_db,save_to_db

url="https://realpython.github.io/fake-jobs/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
create_db()

items=soup.find(id="ResultsContainer")
job_elements=items.find_all("div",class_="card-content")
all_jobs=[]

for job in job_elements:
	title=job.find("h2",class_="title").text.strip()
	company=job.find("h3",class_="company").text.strip()
	location=job.find("p",class_="location").text.strip()
	apply=(job.find("a",class_="card-footer-item"))["href"]
	all_jobs.append(
		{
			"name": title,
			"company": company,
			"location": location, 
			"link":apply
		}
	)
	print(f"Job: {title} | Company: {company} | Location: {location} | Apply-Link:{apply}")
	
save_to_db(all_jobs)