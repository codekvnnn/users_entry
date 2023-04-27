from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "youre a wizard harry" 

@app.route('/')
def index():
    # Connect to the database
    mysql = connectToMySQL('users_schema')

    # Retrieve all users from the database
    results = mysql.query_db('SELECT * FROM users;')
    users = []
    for user in results:
        users.append((user))

    # Render the Read (All) page with the retrieved users
    return render_template('read.html', users=users)

@app.route('/create')
def create():
    # Render the Create page
    print(request.form)
    return render_template('create.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    # Connect to the database
    mysql = connectToMySQL('users_schema')

    # Insert a new user into the database
    # query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'

    mysql.query_db(query, data)

    # Redirect to the Read (All) page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
