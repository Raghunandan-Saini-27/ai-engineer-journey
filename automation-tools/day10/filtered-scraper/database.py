import sqlite3


def create_table():
	conn=sqlite3.connect("database.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS jobs(
					id INTEGER PRIMARY KEY,
					job TEXT,
					company TEXT,
					location TEXT )""")	
	conn.commit()
	conn.close()
	return print({"message":"Table {jobs} created successfully."})

def save_jobs(jobs_list):
	conn=sqlite3.connect("database.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.executemany("""INSERT INTO jobs(job,company,location) VALUES(:job,:company,:location)""",jobs_list)
	conn.commit()
	conn.close()
