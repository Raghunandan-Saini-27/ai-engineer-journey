import requests 
import re
from bs4 import BeautifulSoup
import pandas as pd

url="https://realpython.github.io/fake-jobs/"
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

items=soup.find(id="ResultsContainer")
job_elements=items.find_all("div",class_="card-content")
all_python_jobs=[]

for job in job_elements:
	title=job.find("h2",class_="title").text.strip()
	if "Python" in title:
		company=job.find("h3",class_="company").text.strip()
		location=job.find("p",class_="location").text.strip()
		all_python_jobs.append(
			{
			"Job": title,
			"Company": company,
			"Location": location
			}
		)	
		print(f"Job: {title} | Company: {company} | Location: {location}")

df=pd.DataFrame(all_python_jobs)
df.to_csv("python_jobs_only.csv")