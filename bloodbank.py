#FOR Blood_Banks
#fetch
from flask import Flask, request, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bloodlife"
)

cursor = db.cursor()

# Route: Render Blood Bank Locator Page
@app.route('/bloodbank')
def bloodbank():
    return render_template('bloodbank.html')

@app.route('/')
def home():
    return render_template('bloodbank.html')

# Route: Fetch Blood Banks by Location (API)
@app.route('/get_blood_banks', methods=['GET'])
def get_blood_banks():
    location = request.args.get('location', '').strip().lower()

    if not location:
        return jsonify({"blood_banks": []})  # Return empty list if no location is entered

    query = "SELECT name, address, contact FROM blood_banks WHERE LOWER(location) LIKE %s"
    cursor.execute(query, ('%' + location + '%',))
    blood_banks = cursor.fetchall()

    bloodbank_list = [{"name": b[0], "address": b[1], "contact": b[2]} for b in blood_banks]

    return jsonify({"blood_banks": bloodbank_list})

if __name__ == '__main__':
    app.run(debug=True)