from fastapi import FastAPI
from database.db import get_all_jobs
from typing import Optional

app=FastAPI()

@app.get("/")
def home():
	return {"message":"API working sucessfully."}

@app.get("/jobs")
def jobs():
	all_data=get_all_jobs()
	job_list=[]
	for item in all_data:
		if item.get("title"):  # Check if 'job' key exists and is not empty/None
			job_list.append(item["title"])
	return {"jobs":job_list}

@app.get("/jobs/search/")
def jobs_search_by_name(keyword :str):
	jobs=get_all_jobs()
	keyword=keyword.lower()
	job_list=[]
	for item in jobs:
		title = item.get("title", "").lower()
		if keyword in title:
			job_list.append(item)			
	return {"jobs":job_list}

@app.get("/jobs/location/")
def jobs_search_by_location(location :str):
	jobs=get_all_jobs()
	location=location.lower()
	jobs_list=[]
	for item in jobs:
		job_loc=item.get("location", "").lower()
		if location in job_loc:
			jobs_list.append(item)
	return {"jobs":jobs_list}