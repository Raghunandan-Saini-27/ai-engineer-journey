from database.db import get_all_jobs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_ranked_jobs(keyword: str):
    jobs = get_all_jobs()
    result = []
    
    if not keyword:
        return result
        
    for job in jobs:
        score = score_job(job, keyword)

        if score > 0:
            job["score"] = score
            result.append(job)

    result.sort(key=lambda x: x["score"], reverse=True)

    return result[:10]


def score_job(job, keyword):
    title = job["title"].lower()
    keyword = keyword.lower()

    score = 0
    
    if keyword in title:
        score += 2

    if keyword in job["company"].lower():
        score += 1
        
    if keyword in job["location"].lower():
        score +=1

    return score


def get_ranked_jobs_ml(keyword:str):
    jobs=get_all_jobs()

    if not keyword:
        return []
    
    keyword.strip().lower()

    job_titles=[]
    for job in jobs:
        text = f"{job['title']} {job['company']} {job['location']}"
        job_titles.append(text)
    
    job_titles.insert(0,keyword)

    vectorizer=TfidfVectorizer()
    vectors=vectorizer.fit_transform(job_titles)
    
    similarity=cosine_similarity(vectors[0:1],vectors[1:])
    result=[]

    for i,job in enumerate(jobs):
        
        score=similarity[0][i]
        if score>0:
            job["score"]=float(score)
            result.append(job)

    result.sort(key=lambda x:x["score"],reverse=True)

    return result[:10]
