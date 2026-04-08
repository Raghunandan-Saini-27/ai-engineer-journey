from database.db import get_all_jobs

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