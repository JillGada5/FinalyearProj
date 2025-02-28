from flask import Flask, flash, redirect, url_for, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'bloodlife'
app.secret_key = 'your_secret_key'

# Initialize MySQL
mysql = MySQL(app)

def get_current_max_request_id():
    """Retrieve the current maximum request_id from the database."""
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COALESCE(MAX(request_id), 0) FROM request")  # Adjust table name if needed
    max_id = cursor.fetchone()[0]
    cursor.close()
    return max_id

@app.route('/', methods=['GET', 'POST'])  # Allow both GET and POST
def request_page():
    # Get the current maximum request_id and increment it
    current_max_request_id = get_current_max_request_id()
    request_id = current_max_request_id + 1  # Increment the request_id
    
    donors = []
    if request.method == 'POST':
        blood_group = request.form.get('blood_group')

        if blood_group:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT full_name, email, blood_group FROM donors WHERE TRIM(blood_group) = %s", (blood_group.strip(),))
            donors = cursor.fetchall()  # Fetch matching donors
            cursor.close()

    return render_template('request1.html', request_id=request_id, donors=donors)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        patient_name = request.form['patient_name']
        phone = request.form['phone']
        blood_group = request.form['bloodgroup']
        quantity = request.form['quantity']
        email = request.form['email']
        location = request.form['location']
        address = request.form['address']

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO request (patient_name, phone, blood_group,email, quantity, location, address) 
                  VALUES (%s, %s, %s, %s,%s, %s, %s)''', 
               (patient_name, phone, blood_group,email, quantity, location, address))
        mysql.connection.commit()
        request_id = cursor.lastrowid
        # Fetch matching donors based on blood group
        cursor.execute("SELECT donor_id, full_name, email, blood_group FROM donors WHERE TRIM(blood_group) = %s", (blood_group.strip(),))
        donors = cursor.fetchall()
        cursor.close()
         
        return render_template('request1.html', request_id=request_id, donors=donors) 

    return jsonify({'error': 'Invalid request method.'}), 400


if __name__ == '__main__':
    app.run(debug=True)
        
        

