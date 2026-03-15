import sqlite3

def create_connection():
	conn=sqlite3.connect("products.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.execute("""
	CREATE TABLE IF NOT EXISTS PRODUCTS
	( id INTEGER PRIMARY KEY,
	name TEXT,
	price INTEGER,
	quantity INTEGER )
	""")
	conn.commit()
	conn.close()

def add_product_to_db(product):
	conn=sqlite3.connect("products.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.executemany("""INSERT INTO PRODUCTS(name,price,quantity) VALUES(?,?,?)""",product)
	conn.commit()
	conn.close()

def get_all_products():
	conn=sqlite3.connect("products.db",check_same_thread=False)
	conn.row_factory = sqlite3.Row
	cursor=conn.cursor()
	cursor.execute("SELECT * FROM PRODUCTS")
	rows=cursor.fetchall()
	conn.close()
	return rows
	
def update_the_product(updated_product):
	conn=sqlite3.connect("products.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.executemany("UPDATE PRODUCTS SET name=?, price=?, quantity=? WHERE id=?",updated_product)
	changes=conn.total_changes
	conn.commit()
	conn.close()
	return changes

def delete_the_product(product_id):
	conn=sqlite3.connect("products.db",check_same_thread=False)
	cursor=conn.cursor()
	cursor.execute("DELETE FROM PRODUCTS WHERE id=?",(product_id,))
	conn.commit()
	deleted_row=cursor.rowcount
	conn.close()
	return deleted_row