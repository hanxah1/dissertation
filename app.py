import os
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import json

app = Flask(__name__)

DATABASE = 'locations.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template('home.html')


@app.route("/tool")
def toolPage():
    conn = get_db_connection()
    locations = conn.execute('SELECT * FROM locations').fetchall()
    conn.close()
    return render_template('tool.html', locations=locations)
