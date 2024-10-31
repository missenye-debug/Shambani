from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

@app.route('/')
def hello ():
    return "Hello, World!"

def get_db_connection():
    conn = sqlite3.connect('Shambani.db')
    conn.row_factory = sqlite3.Row
    return conn

import sqlite3
def init_db():
    conn=sqlite3.connect('Shambani.db')
    cursor = conn.cursor()
    conn.close ()

def index():
    conn=get_db_connection()
    schedules= conn.execute('SELECT * FROM schedule').fetchall()
    conn.close()
    return render_template ('index.html', schedules=schedules)

def add():
    if request.method == 'POST':
        start_time = request.form ['start_time']
        duration = int(request.form['duration'])
        conn = get_db_connection()
        conn.execute('INSERT INTO schedule(start_time, duration) VALUES (?, ?)', start_time,duration)
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__': 
    init_db()
    app.run(debug=True)

    



