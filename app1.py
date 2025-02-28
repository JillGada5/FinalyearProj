from flask import Flask, request, render_template, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  # Set your MySQL password
    database="bloodlife"
)

cursor = db.cursor()

@app.route('/')
def admin_panel():
    return render_template('admin_panel.html')

@app.route('/add_hospital', methods=['POST'])
def add_hospital():
    name = request.form['name']
    contact = request.form['contact']
    address = request.form['address']
    location = request.form['location']

    cursor.execute("INSERT INTO hospitals (name, contact, address, location) VALUES (%s, %s, %s, %s)", 
                   (name, contact, address, location))
    db.commit()
    return jsonify({"message": "Hospital added successfully!"})

@app.route('/add_bloodbank', methods=['POST'])
def add_bloodbank():
    name = request.form['name']
    contact = request.form['contact']
    address = request.form['address']
    location = request.form['location']

    cursor.execute("INSERT INTO blood_banks (name, contact, address, location) VALUES (%s, %s, %s, %s)", 
                   (name, contact, address, location))
    db.commit()
    return jsonify({"message": "Blood Bank added successfully!"})

@app.route('/add_event', methods=['POST'])
def add_event():
    name = request.form['name']
    event_date = request.form['event_date']
    location = request.form['location']
    description = request.form['description']

    cursor.execute("INSERT INTO events (name, event_date, location, description) VALUES (%s, %s, %s, %s)", 
                   (name, event_date, location, description))
    db.commit()
    return jsonify({"message": "Event added successfully!"})


@app.route('/get_hospitals', methods=['GET'])
def get_hospitals():
    cursor.execute("SELECT name, contact, address, location FROM hospitals")
    hospitals = cursor.fetchall()
    return jsonify(hospitals)

@app.route('/get_bloodbanks', methods=['GET'])
def get_bloodbanks():
    cursor.execute("SELECT name, contact, address, location FROM blood_banks")
    blood_banks = cursor.fetchall()
    return jsonify(blood_banks)

@app.route('/get_events', methods=['GET'])
def get_events():
    cursor.execute("SELECT name, event_date, location, description FROM events")
    events = cursor.fetchall()
    return jsonify(events)
'''@app.route('/get_donors', methods=['GET'])
def get_donors():
    cursor = db.cursor(dictionary=True)  # Get column names
    cursor.execute("SELECT donor_id, full_name, dob, blood_group, gender, email, phone, current_location, available_location FROM donors")
    donors = cursor.fetchall()
    cursor.close()  
    return jsonify(donors)'''




if __name__ == '__main__':
    app.run(debug=True)
