import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://realpython.github.io/fake-jobs/"
responses=requests.get(url)
soup=BeautifulSoup(responses.text,'html.parser')

items=soup.find(id="ResultsContainer")
job_elements=items.findAll("div",class_="card-content")
all_jobs=[]
for job in job_elements:
	title=job.find("h2",class_="title").text.strip()
	company = job.find("h3", class_="company").text.strip()
	location = job.find("p",class_="location").text.strip()
	all_jobs.append({
        "Job Title": title,
        "Company": company,
        "Location": location
    })
	print(f"Job: {title} | Company: {company}")

df=pd.DataFrame(all_jobs)
df.to_csv("python_jobs.csv",index=False)