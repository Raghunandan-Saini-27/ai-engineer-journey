import sqlite3

conn=sqlite3.connect("jobs.db")
cursor=conn.cursor()

def create_db():
	conn=sqlite3.connect("jobs.db")
	cursor=conn.cursor()
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS jobs(
				id INTEGER PRIMARY KEY,
				name TEXT,
				company TEXT,
				location TEXT,
				link TEXT
				)""")
	conn.commit()
	conn.close()

def save_to_db(job_list):
	conn=sqlite3.connect("jobs.db")
	cursor=conn.cursor()
	cursor.executemany("""INSERT INTO jobs(name,company,location,link) VALUES(:name, :company, :location, :link)""",job_list)
	conn.commit()
	conn.close()