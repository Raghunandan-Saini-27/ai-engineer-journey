import sqlite3

def create_table():
	conn=sqlite3.connect("database.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS predictions(
				id INTEGER PRIMARY KEY,
				user_input INTEGER,
				model_output INTEGER)""")
	conn.commit()
	conn.close()
	return print("Table Created Sucessfully.")

def add_prediction_to_db(data):
	conn=sqlite3.connect("database.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.executemany("""INSERT INTO predictions(user_input,model_output) VALUES(?,?)""",data)
	conn.commit()
	conn.close()
	return {"message":"Prediction saved to db sucessfully."}

def return_all_pred():
	conn=sqlite3.connect("database.db",check_same_thread=False)
	conn.row_factory = sqlite3.Row
	cursor=conn.cursor()
	cursor.execute("SELECT * FROM predictions")
	rows=cursor.fetchall()
	conn.close()
	return rows