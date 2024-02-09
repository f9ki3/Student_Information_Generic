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

# Function to insert data into the database
def insert_data(first_name, last_name, age, birthdate, address, email, year_level, school_year):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, age, birthdate, address, email, year_level, school_year) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, age, birthdate, address, email, year_level, school_year))
    conn.commit()
    conn.close()


# Function to retrieve all students from the database
def get_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

# Function to delete student from the database
def delete_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

# Function to update student information
def update_student(student_id, name, section):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, section=? WHERE id=?", (name, section, student_id))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        section = request.form['section']
        insert_data(name, section)
        return redirect(url_for('index'))
    else:
        students = get_students()
        return render_template('index.html', students=students)

@app.route('/delete/<int:student_id>')
def delete(student_id):
    delete_student(student_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit(student_id):
    if request.method == 'POST':
        name = request.form['name']
        section = request.form['section']
        update_student(student_id, name, section)
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
        student = cursor.fetchone()
        conn.close()
        return render_template('edit.html', student=student)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
