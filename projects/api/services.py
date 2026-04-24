from database.db import get_all_jobs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

vectorizer=None
job_vectors=None
job_cache=None


def clean_text(text):
    text=text.strip().lower()
    text=re.sub(r"[^a-zA-Z0-9 ]", "",text)
    text = re.sub(r"\s+", " ", text)
    return text


def score_job(job,keywords):
    title = clean_text(job["title"])
    company = clean_text(job["company"])
    location = clean_text(job["location"])
    rule_score = 0
    for word in keywords:
        if word in title:
            rule_score += 2

        if word in company:
            rule_score += 1
        
        if word in location:
            rule_score +=1

    return rule_score

def initialize_vectors():
    jobs=get_all_jobs()
    jobs_text=[]
    for job in jobs:
        raw_text=f"{job['title']} {job['company']} {job['location']}"
        cleaned_text=clean_text(raw_text)
        jobs_text.append(cleaned_text)

    MAX_FEATURES=500
    global vectorizer,job_vectors,job_cache
    vectorizer=TfidfVectorizer(stop_words="english",max_features=MAX_FEATURES,min_df=2)
    vectorizer.fit(jobs_text)

    job_vectors=vectorizer.transform(jobs_text)
    job_cache=jobs

def refresh_vectors():
    initialize_vectors()

def get_ranked_jobs(keyword: str):
    global job_cache
    job_copy=[job.copy() for job in job_cache]
    keyword=clean_text(keyword)
    result = []
    
    if not keyword:
        return result
        
    for job in job_copy:
        score = score_job(job, keyword)

        if score > 0:
            job["score"] = score
            result.append(job)

    result.sort(key=lambda x: x["score"], reverse=True)

    return result[:10]

def get_ranked_jobs_hybrid(keyword:str):
    global vectorizer, job_vectors, job_cache

    keyword=clean_text(keyword)
    keywords=keyword.split()
    if not keywords :
        return []
    
    if vectorizer is None or job_vectors is None:
        return []
    
    query_vec=vectorizer.transform([keyword])

    similarity=cosine_similarity(query_vec,job_vectors)

    result=[]
    for i,job in enumerate(job_cache):
        ml_score=similarity[0][i]
        rule_score=score_job(job,keywords)
        final_score=(0.5*rule_score)+ml_score
           
        if final_score>0:
            job_copy=job.copy()
            job_copy['score']=float(final_score)
            result.append(job_copy)

    result.sort(key=lambda x:x['score'],reverse=True)

    return result[:10]

def get_filtered_ranked_jobs(keyword:str,location:str):
    global job_cache,job_vectors

    keyword=clean_text(keyword)
    keywords=keyword.split()

    location=clean_text(location)
    if not location:
        return job_cache[:10]

    if vectorizer is None or job_vectors is None:
        return []
    
    filtered_jobs=[]
    filtered_indices=[]
    for i,job in enumerate(job_cache):
        if location in clean_text(job["location"]) :
            filtered_jobs.append(job)
            filtered_indices.append(i)

    result=[]
    query_vec=vectorizer.transform([keyword])
    similarity=cosine_similarity(query_vec,job_vectors)

    for idx,job in zip(filtered_indices,filtered_jobs):
        ml_score=similarity[0][idx]
        rule_score=score_job(job,keywords)
        final_score=ml_score+(rule_score*0.5)

        if final_score>0:
            job_copy=job.copy()
            job_copy["score"]=float(final_score)
            result.append(job_copy)
    result.sort(key=lambda x: x["score"], reverse=True)

    return result[:10]
