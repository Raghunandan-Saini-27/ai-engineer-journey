import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def create_jobs_table():		#Creating table named jobs
	conn=sqlite3.connect(DB_PATH,check_same_thread=False)
	cursor=conn.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS jobs(
				id INTEGER PRIMARY KEY,
				title TEXT,
				company TEXT,
				location TEXT,
				link TEXT UNIQUE)""")
	conn.commit()
	conn.close()

def insert_job(jobs:list):		#Adding job(title,company,location,link) 
	conn=sqlite3.connect(DB_PATH,check_same_thread=False)
	cursor=conn.cursor()
	cursor.executemany("""INSERT OR IGNORE INTO jobs(title,company,location,link) VALUES(:title, :company, :location, :link)""",jobs)
	conn.commit()
	conn.close()

def get_all_jobs(limit: int = None, offset: int = 0):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if limit is not None:
        query = "SELECT * FROM jobs LIMIT ? OFFSET ?"
        cursor.execute(query, (limit, offset))
    else:
        query = "SELECT * FROM jobs"
        cursor.execute(query)

    rows = cursor.fetchall()
    jobs_list = [dict(row) for row in rows]

    conn.close()
    return jobs_list

def search_jobs_by_title(keyword: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = "SELECT * FROM jobs WHERE LOWER(title) LIKE ?"
    cursor.execute(query, (f"%{keyword.lower()}%",))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

def search_jobs_by_location(location: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = "SELECT * FROM jobs WHERE LOWER(location) LIKE ?"
    cursor.execute(query, (f"%{location.lower()}%",))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]