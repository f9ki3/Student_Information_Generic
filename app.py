# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create SQLite database table if not exists
def create_table():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                      id INTEGER PRIMARY KEY,
                      first_name TEXT,
                      last_name TEXT,
                      age INTEGER,
                      birthdate TEXT,
                      address TEXT,
                      email TEXT,
                      year_level INTEGER,
                      school_year TEXT
                      )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
        
        return render_template('index.html')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
