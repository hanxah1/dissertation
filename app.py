import os
from flask import Flask, g, render_template, request, redirect, url_for, jsonify
import sqlite3
# import json

app = Flask(__name__)

DATABASE = 'locations.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        return db

def get_db_connection():
    conn = sqlite3.connect('locations.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/tool', methods=['GET'])
def get_locations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM locations') 
    rows = cursor.fetchall()
    conn.close()


    locations = []
    for row in rows:
        locations.append({
            'name': row[2],
            'lat': row[7],
            'long': row[8],
            'phone': row[4],
            'email': row[1],
            'postcode': row[0],
            'times': row[3],
            'classes': row[10],
            'prices': row[9],
            'website': row[6],
            'keywords':row[5]
        })

    return render_template('tool.html', results=jsonify(locations))
    

@app.route('/markers')
def get_markers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM locations')  
    rows = cursor.fetchall()
    conn.close()


    locations = []
    for row in rows:
        locations.append({
            'name': row[2],
            'lat': row[7],
            'long': row[8],
            'phone': row[4],
            'email': row[1],
            'postcode': row[0],
            'times': row[3],
            'classes': row[10],
            'prices': row[9],
            'website': row[6],
            'keywords':row[5]
        })

    return jsonify(locations)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()    

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)

    