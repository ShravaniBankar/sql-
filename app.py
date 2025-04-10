from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'store.db')


@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 🚨 VULNERABLE LOGIN
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            user = cursor.fetchone()
        except Exception as e:
            return f"<h3>SQL Error: {e}</h3>"

        if user:
            return redirect('/home')
        else:
            error = "Invalid credentials"

    return render_template('login.html', error=error)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/search', methods=['GET'])
def search_products():
    search = request.args.get('search', '')

    if not search:
        return render_template('search.html', products=None)

    # 🚨 VULNERABLE SEARCH
    query = f"SELECT * FROM products WHERE name LIKE '%{search}%' OR category LIKE '%{search}%'"

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        products = cursor.fetchall()
    except Exception as e:
        return f"<h3>SQL Error: {e}</h3>"

    return render_template('search.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
