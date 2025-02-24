from flask import Flask, request, render_template, jsonify,redirect,url_for
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

# Route: Search Hospitals by Location (HTML Page)


@app.route('/search_hospital')
def search_hospital():
    return render_template('search_hospital.html')


@app.route('/')
def home():
    return render_template('search_hospital.html')
    


# Route: Fetch Hospitals by Location (API)
@app.route('/get_hospitals', methods=['GET'])
def get_hospitals():
    location = request.args.get('location', '').lower()

    if not location:
        return jsonify({"hospitals": []})

    query = "SELECT name, address, contact FROM hospitals WHERE LOWER(location) LIKE %s"
    cursor.execute(query, ('%' + location + '%',))
    hospitals = cursor.fetchall()

    hospital_list = [{"name": hospital[0], "address": hospital[1], "contact": hospital[2]} for hospital in hospitals]

    return jsonify({"hospitals": hospital_list})

if __name__ == '__main__':
    app.run(debug=True)