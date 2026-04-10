from fastapi import FastAPI
from database.db import get_all_jobs,search_jobs_by_location,search_jobs_by_title
from api.services import get_ranked_jobs,get_ranked_jobs_ml

app=FastAPI()

@app.get("/")
def home():
	return {"message":"API working sucessfully."}

@app.get("/jobs")
def jobs(page: int=1,limit: int=10):
	# Prevent negative pages
    if page < 1:
        page = 1
        
    offset = (page - 1) * limit
    
    # Only fetch what is needed
    job_titles = get_all_jobs(limit, offset)
    
    return {"jobs": job_titles}

@app.get("/jobs/search")
def jobs_search(keyword: str):
    return {"jobs": search_jobs_by_title(keyword)}

@app.get("/jobs/location")
def jobs_search_by_location(location: str):
    return {"jobs": search_jobs_by_location(location)}

@app.get("/jobs/ranked")
def ranked_jobs(keyword : str):
    return get_ranked_jobs(keyword)

@app.get("/jobs/ranked-ml")
def ranked_ml_jobs(keyword:str):
     return get_ranked_jobs_ml(keyword)