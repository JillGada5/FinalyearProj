from flask import Flask, request, render_template, jsonify
from collections import OrderedDict
from datetime import datetime
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  # Set your MySQL password
    database="bloodlife"
)

@app.route('/')
def admin_panel():
    return render_template('admin_panel.html')

@app.route('/add_hospital', methods=['POST'])
def add_hospital():
    name = request.form['name']
    contact = request.form['contact']
    address = request.form['address']
    location = request.form['location']

    cursor = db.cursor()
    cursor.execute("INSERT INTO hospitals (name, contact, address, location) VALUES (%s, %s, %s, %s)", 
                   (name, contact, address, location))
    db.commit()
    cursor.close()
    return jsonify({"message": "Hospital added successfully!"})

@app.route('/add_bloodbank', methods=['POST'])
def add_bloodbank():
    name = request.form['name']
    contact = request.form['contact']
    address = request.form['address']
    location = request.form['location']

    cursor = db.cursor()
    cursor.execute("INSERT INTO blood_banks (name, contact, address, location) VALUES (%s, %s, %s, %s)", 
                   (name, contact, address, location))
    db.commit()
    cursor.close()
    return jsonify({"message": "Blood Bank added successfully!"})

@app.route('/add_event', methods=['POST'])
def add_event():
    name = request.form['name']
    event_date = request.form['event_date']
    location = request.form['location']
    description = request.form['description']

    cursor = db.cursor()
    cursor.execute("INSERT INTO events (name, event_date, location, description) VALUES (%s, %s, %s, %s)", 
                   (name, event_date, location, description))
    db.commit()
    cursor.close()
    return jsonify({"message": "Event added successfully!"})

@app.route('/get_hospitals', methods=['GET'])
def get_hospitals():
    cursor = db.cursor(dictionary=True)  # Use dictionary cursor
    cursor.execute("SELECT name, contact, address, location FROM hospitals")
    hospitals = cursor.fetchall()
    cursor.close()
    return jsonify(hospitals)

@app.route('/get_bloodbanks', methods=['GET'])
def get_bloodbanks():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT name, contact, address, location FROM blood_banks")
    blood_banks = cursor.fetchall()
    cursor.close()
    return jsonify(blood_banks)

@app.route('/get_events', methods=['GET'])
def get_events():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT name, event_date, location, description FROM events")
    events = cursor.fetchall()
    cursor.close()
    return jsonify(events)

@app.route('/get_donors', methods=['GET'])
def get_donors():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM donors")  # Assuming 'donors' is the table name
    donors = cursor.fetchall()
    cursor.close()
    return jsonify(donors)


if __name__ == '__main__':
    app.run(debug=True)
