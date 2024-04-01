from flask import Flask, render_template, request, redirect, session
import mysql.connector
import hashlib
import secrets
import string


secret_key = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(64))


app = Flask(__name__)
app.secret_key = secret_key #Make sure to keep your secret key secure and never share or commit it to version control systems or other public places.


# MySQL database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Suyash@6237",
    database="registration_db"
)

@app.route('/')
def index():
    if 'user' in session:
        return render_template('welcome.html')
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_name = request.form['student_name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        blood_group = request.form['blood_group']
        department = request.form['department']
        course = request.form['course']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        cursor = mydb.cursor()
        sql = "INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password)
        cursor.execute(sql, values)
        mydb.commit()
        cursor.close()

        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        cursor = mydb.cursor()
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        values = (email, password)
        cursor.execute(sql, values)
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['user'] = {
                'id': user[0],
                'student_name': user[1],
                'email': user[5]
            }
            return redirect('/')
        else:
            return 'Invalid email or password'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)