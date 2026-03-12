import sqlite3


def create_connection():
	conn=sqlite3.connect("store.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.execute("""
	CREATE TABLE IF NOT EXISTS PRODUCTS
	( id INTEGER PRIMARY KEY,
	name TEXT,
	price INTEGER )
			   """)
	conn.commit()
	conn.close()

def add_product_to_db(products_list):
	conn=sqlite3.connect("store.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.executemany("""INSERT INTO PRODUCTS(name,price) VALUES(?,?)""",products_list)
	conn.commit()
	conn.close()

def get_all_products():
	conn=sqlite3.connect("store.db",check_same_thread=False)
	conn.row_factory = sqlite3.Row
	cursor=conn.cursor()
	cursor.execute("SELECT * FROM PRODUCTS")
	rows=cursor.fetchall()
	conn.close()
	return rows

def get_total_price():
	conn=sqlite3.connect("store.db",check_same_thread=False)
	conn.row_factory = sqlite3.Row
	cursor=conn.cursor()
	cursor.execute("SELECT SUM(price) FROM PRODUCTS")
	result = cursor.fetchone()
	conn.close()
	return result[0] if result[0] is not None else 0
