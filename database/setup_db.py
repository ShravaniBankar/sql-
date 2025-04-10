import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'store.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Create products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL
)
''')

# Insert sample users
cursor.executemany('INSERT INTO users (username, password) VALUES (?, ?)', [
    ('admin', 'admin123'),
    ('user1', 'password1')
])

# Insert sample products
cursor.executemany('INSERT INTO products (name, category) VALUES (?, ?)', [
    ('iPhone 13', 'electronics'),
    ('Samsung TV', 'electronics'),
    ('Nike Shoes', 'fashion'),
    ('Adidas Jacket', 'fashion')
])

conn.commit()
conn.close()
print("✅ Database setup complete.")
