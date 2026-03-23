import requests
from bs4 import BeautifulSoup
from database import create_table,save_jobs

create_table()
url="https://realpython.github.io/fake-jobs/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")


items=soup.find(id="ResultsContainer")
job_cards=items.find_all("div",class_="card-content")
all_jobs=[]
for job in job_cards:
	title=job.find("h2",class_="title").text.strip()
	if "Python" in title :
		company=job.find("h3",class_="company").text.strip()
		location=job.find("p",class_="location").text.strip()
		if "AA" in location:
			apply=(job.find("a",class_="card-footer-item"))["href"]
			all_jobs.append(
				{
				"job": title,
				"company": company,
				"location": location
				}
			)
			print(f"Job: {title} | Company: {company} | Location: {location}")

save_jobs(all_jobs)