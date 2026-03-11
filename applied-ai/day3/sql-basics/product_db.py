import sqlite3

conn=sqlite3.connect("products.db")

cursor=conn.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS products(
			   id INTEGER PRIMARY KEY,
			   name TEXT,
			   price INTEGER,
			   quantity INTEGER
			   )	
""")

products_list=[("Laptop", 800, 50),
			   ("Phone", 500, 8),
			   ("Tablet", 300, 6)]

cursor.executemany("INSERT INTO products(name,price,quantity) VALUES (?,?,?)",products_list)	#Inserting sample data
cursor.execute("UPDATE products SET revenue = price * quantity")

try :
	cursor.execute("ALTER TABLE products ADD COLUMN revenue INTEGER")

except sqlite3.OperationalError:
	print("Column 'revenue' already exists, skipping...")

conn.commit()

cursor.execute("SELECT * FROM products")
rows=cursor.fetchall()

for row in rows:
	print(row)

conn.close()