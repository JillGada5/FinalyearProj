# For Admin
from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

@app.route('/')
def home():
    return redirect(url_for('admin_login'))

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True  # Store login status in session
            return redirect(url_for('admin_panel1'))  # Redirect to admin panel
        else:
            return render_template('admin_login.html', error="Invalid Username or Password!")

    return render_template('admin_login.html')

@app.route('/admin_panel1')  # Ensure route name matches function name
def admin_panel1():  # Function name should match the route
    if not session.get('admin_logged_in'):  # Check if admin is logged in
        return redirect(url_for('admin_login'))  # Redirect if not logged in
    return render_template('admin_panel1.html')

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)  # Remove login session
    return redirect(url_for('admin_login'))  # Redirect to login page

if __name__ == '__main__':
    app.run(debug=True)
