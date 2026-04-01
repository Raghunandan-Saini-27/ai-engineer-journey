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

def insert_job(job):		#Adding job(title,company,location,link) 
	conn=sqlite3.connect(DB_PATH,check_same_thread=False)
	cursor=conn.cursor()
	cursor.executemany("""INSERT OR IGNORE INTO jobs(title,company,location,link) VALUES(:title, :company, :location, :link)""",job)
	conn.commit()
	conn.close()


def get_all_jobs():			#Getting entire table fetched
	conn=sqlite3.connect(DB_PATH,check_same_thread=False)
	conn.row_factory = sqlite3.Row
	cursor=conn.cursor()
	cursor.execute("SELECT * FROM jobs")
	rows=cursor.fetchall()
	jobs_list = [dict(row) for row in rows]
	return jobs_list