from flask import Flask, request, g
import sqlite3

app = Flask(__name__)

DATABASE = 'store.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def home():
    return "Welcome to the Product Store! Visit /products?category=electronics"

@app.route('/products')
def get_products():
    category = request.args.get('category', '')

    #  SQL Injection Vulnerability 
    query = f"SELECT * FROM products WHERE category = '{category}'"
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query)
    products = cursor.fetchall()

    return f"Products: {products}"

if __name__ == "__main__":
    app.run(debug=True)
