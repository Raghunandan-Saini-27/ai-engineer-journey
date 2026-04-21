from database.db import get_all_jobs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def clean_text(text):
    text=text.strip().lower()
    text=re.sub(r"[^a-zA-Z0-9 ]", "",text)
    text = re.sub(r"\s+", " ", text)
    return text

def get_ranked_jobs(keyword: str):
    jobs = get_all_jobs()
    job_copy=[job.copy() for job in jobs]
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


def score_job(job, keyword):
    title = clean_text(job["title"])
    company = clean_text(job["company"])
    location = clean_text(job["location"])

    score = 0
    
    if keyword in title:
        score += 2

    if keyword in company:
        score += 1
        
    if keyword in location:
        score +=1

    return score


def get_ranked_jobs_ml(keyword:str):
    jobs=get_all_jobs()
    job_copy=[job.copy() for job in jobs]

    keyword=clean_text(keyword)
    if not keyword:
        return []
    
    job_texts=[]
    for job in job_copy:
        raw_text = f"{job['title']} {job['company']} {job['location']}"
        cleaned_text=clean_text(raw_text)
        job_texts.append(cleaned_text)
    
    job_texts.insert(0,keyword)

    MAX_FEATURES=100
    vectorizer=TfidfVectorizer(stop_words="english",max_features=MAX_FEATURES,min_df=2)
    vectors=vectorizer.fit_transform(job_texts)
    
    similarity=cosine_similarity(vectors[0:1],vectors[1:])
    result=[]

    for i,job in enumerate(job_copy):
        
        score=similarity[0][i]
        if score>0: 
            job["score"]=float(score)
            result.append(job)

    result.sort(key=lambda x:x["score"],reverse=True)

    return result[:10]
