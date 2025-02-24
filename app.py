from flask import Flask, flash, redirect, url_for, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'bloodlife'
app.secret_key = 'your_secret_key'

# Simulated donor ID for demonstration purposes
donor_id_counter = 0

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    # Get the donor_id from the query parameters
    donor_id = request.args.get('donor_id', default='1')  # Get the donor ID from the query parameters
    return render_template('index.html', donor_id=donor_id)  # Render your HTML form

@app.route('/submit', methods=['POST'])
def submit():
    
    if request.method == 'POST':
        # Get form data
        full_name = request.form['fullName']
        dob = request.form['dob']
        blood_group = request.form['bloodGroup']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        current_location = request.form['currentLocation']
        # Get available locations (this will be a list)
        available_locations = request.form.getlist('availableLocation')  # Ensure this line is correct
        # Join the list into a single string, separated by commas (or any other delimiter)
        available_location = ', '.join(available_locations)
     

        # Insert data into MySQL database
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO donors (full_name, dob, blood_group, gender, email, phone, current_location, available_location) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', 
                       (full_name, dob, blood_group, gender, email, phone, current_location, available_location))
        mysql.connection.commit()
        donor_id = cursor.lastrowid
        cursor.close()

        
        

        # Redirect to the index route with the donor_id as a query parameter
        return redirect(url_for('index', donor_id=donor_id))  # Pass donor_id to the index route

    # If the request method is not POST, return an error
    return jsonify({'error': 'Invalid request method.'}), 400

if __name__ == '__main__':
    app.run(debug=True)