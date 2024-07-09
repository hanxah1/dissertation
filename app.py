import os
from flask import Flask, g, render_template, request, redirect, url_for
import sqlite3
# import json

app = Flask(__name__)

DATABASE = 'locations.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        return db
    # conn = sqlite3.connect(DATABASE)
    # conn.row_factory = sqlite3.Row
    # return conn

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()    

@app.route("/")
def index():
    return render_template('home.html')


@app.route("/tool")
def toolPage():
    db = get_db()
    cursor = db.execute('SELECT * FROM locations')
    results = cursor.fetchall()
    # conn = get_db_connection()
    # locations = conn.execute('SELECT * FROM locations').fetchall()
    # conn.close()
    return render_template('tool.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)