app1.py
from flask import Flask, request, render_template, redirect, url_for, jsonify, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  # Set your MySQL password
    database="bloodlife"
)

cursor = db.cursor()

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

# Route: Admin Login Page
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True  # Store login status in session
            return redirect(url_for('admin_panel'))
        else:
            return render_template('admin_login.html', error="Invalid Username or Password!")

    return render_template('admin_login.html')

# Route: Admin Panel (Protected)
@app.route('/')
def admin_panel():
    if 'admin_logged_in' not in session or not session['admin_logged_in']:  # Fix: Proper session check
        return redirect(url_for('admin_login'))
    return render_template('admin_panel.html')

# Route: Logout
@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)  # Remove login session
    return redirect(url_for('admin_login'))

# Route: Add Hospital (Admin Only)
@app.route('/add_hospital', methods=['POST'])
def add_hospital():
    if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return jsonify({"message": "Unauthorized access"}), 403

    name = request.form['name']
    contact = request.form['contact']
    address = request.form['address']
    location = request.form['location']

    cursor.execute("INSERT INTO hospitals (name, contact, address, location) VALUES (%s, %s, %s, %s)", 
                   (name, contact, address, location))
    db.commit()
    return jsonify({"message": "Hospital added successfully!"})

# Route: Add Blood Bank (Admin Only)
@app.route('/add_bloodbank', methods=['POST'])
def add_bloodbank():
    if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return jsonify({"message": "Unauthorized access"}), 403

    name = request.form['name']
    contact = request.form['contact']
    address = request.form['address']
    location = request.form['location']

    cursor.execute("INSERT INTO blood_banks (name, contact, address, location) VALUES (%s, %s, %s, %s)", 
                   (name, contact, address, location))
    db.commit()
    return jsonify({"message": "Blood Bank added successfully!"})

# Route: Add Event (Admin Only)
@app.route('/add_event', methods=['POST'])
def add_event():
    if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return jsonify({"message": "Unauthorized access"}), 403

    name = request.form['name']
    event_date = request.form['event_date']
    location = request.form['location']
    description = request.form['description']

    cursor.execute("INSERT INTO events (name, event_date, location, description) VALUES (%s, %s, %s, %s)", 
                   (name, event_date, location, description))
    db.commit()
    return jsonify({"message": "Event added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)