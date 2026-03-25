from fastapi import FastAPI
from database.db import get_all_jobs

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

@app.get("/jobs/python")
def jobs_python():
	python_jobs=get_all_jobs()
	job_list=[]
	for item in python_jobs:
		if "Python" in item.get("title"):
			job_list.append(item["title"])			
	return {"jobs":job_list}
