# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#These are the models and classes
class Database():
        def __init__(self):
              self.conn = sqlite3.connect('student.db')

        # Method to create SQLite database table if not exists
        def create_table(self):
            conn = self.conn
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            middle_name TEXT,
                            section_name TEXT,
                            status_name TEXT,
                            school_year TEXT,
                            address TEXT,
                            birthdate TEXT,
                            age INTEGER,
                            contact INTEGER,
                            email TEXT,
                            guardian TEXT,
                            guardian_email TEXT
                            )''')
            conn.commit()
            conn.close()

#now lets create a class for our students functionalities
class Student():
        def __init__ (self):
            self.conn = Database().conn

        def insertStudentRecords(self, fname, lname, mname, section, status, sy, address, bday, age, contact, email, guardian, guardian_email):
            conn = self.conn
            data = fname, lname, mname, section, status, sy, address, bday, age, contact, email, guardian, guardian_email
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO students (first_name, last_name, middle_name, section_name, status_name, school_year, address, birthdate, age, contact, email, guardian, guardian_email)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', data)
            conn.commit()
            conn.close()
            print("Student Record Added Success!")

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
        return ('Add Student')

if __name__ == '__main__':
    Database().create_table()
    Student().insertStudentRecords('Fyke', 'Lleva', 'Dela Cruz', 'BSIT42B', 'Regular', '2023-2024', 'Loma De Gato', 'January 1st 1990', 34, 9120912091, 'floterina@gmail.com', 'Danielle Laurence', 'danielle@gmail.com')
    app.run(debug=True)
