import sqlite3

# Connect to SQLite database (creates store.db if not exists)
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Create 'products' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL
)
''')

# Sample data to insert (must be a list of tuples)
products = [
    ('iPhone 13', 'electronics'),
    ('Samsung TV', 'electronics'),
    ('Nike Shoes', 'fashion'),
    ('Adidas Jacket', 'fashion')
]

# Insert data into the table
cursor.executemany('INSERT INTO products (name, category) VALUES (?, ?)', products)

# Commit changes and close the database connection
conn.commit()
conn.close()

print("Database setup complete.")
