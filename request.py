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

@app.route('/')
def request_page():
    # Get the current maximum request_id and increment it
    current_max_request_id = get_current_max_request_id()
    request_id = current_max_request_id + 1  # Increment the request_id
    return render_template('request.html', request_id=request_id)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        patient_name = request.form['patient_name']
        email = request.form['email']
        phone = request.form['phone']
        blood_group = request.form['bloodgroup']
        quantity = request.form['quantity']
        location = request.form['location']
        address = request.form['address']

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO request (patient_name,email, phone, blood_group, quantity, location, address) 
                  VALUES (%s,%s,%s, %s, %s, %s, %s)''', 
               (patient_name,email, phone, blood_group, quantity, location, address))
        mysql.connection.commit()
        request_id = cursor.lastrowid
        cursor.close()
         
        return redirect(url_for('request_page', request_id=request_id)) 
    
    return jsonify({'error': 'Invalid request method.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
        
        

