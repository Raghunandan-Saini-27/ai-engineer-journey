import requests 
from bs4 import BeautifulSoup
from database.db import create_jobs_table, insert_job
from api.services import refresh_vectors


url="https://realpython.github.io/fake-jobs/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

items=soup.find(id="ResultsContainer")
job_cards=items.find_all("div",class_="card-content")

create_jobs_table()
job=[]
for in_job in job_cards:
	title=in_job.find("h2",class_="title").text.strip()
	company=in_job.find("h3",class_="company").text.strip()
	location=in_job.find("p",class_="location").text.strip()
	link=(in_job.find("a",class_="card-footer-item"))["href"]
	job.append({"title":title,
			 "company":company,
			 "location":location,
			 "link":link})
	print(f"Job :{title} | Company :{company} |Location :{location} | Link :{link}")
insert_job(job)

refresh_vectors()
