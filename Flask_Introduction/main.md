
# app.py

# To run the Flask app, use the command:
# python app.py
# Make sure to install Flask first:
# pip3 install Flask
# This code sets up a simple Flask web application that returns "Hello, Flask! 🎉" when accessed at the root URL.
# This is a basic Flask application that serves a simple "Hello, Flask!" message.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask! 🎉'

if __name__ == '__main__':
    app.run(debug=True)


## ▶️ 2. Run the Flask app

In your terminal (with virtual environment activated):

python app.py

You should see output like:

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


## 🛠 Tip: Want to auto-reload when you change the code?

Set the FLASK_ENV to development. This enables debug mode.
Linux/macOS:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run


## SQL Alchemy  VS flask-alchemy
# SQL Alchemy
-SQL Alchemy is a powerful SQL toolkit and Object Relational Mapper (ORM) for Python.
-It is a powerful python library that provides a set of high level API tools for working with relational databases.
# flask-alchemy
-flask-alchemy is a Flask extension that adds SQL Alchemy support to Flask applications.
-It adds SQLAlchey support ti a Flask Application.
-It is a wrapper around SQL Alchemy that makes it easier to use with Flask.

## Feature |             SQLAlchemy                            |               Flask-SQLAlchemy
What it is | A powerful database toolkit and ORM for Python    | A Flask extension that integrates SQLAlchemy with Flask
Use Case   | Standalone Python apps or advanced setups         |         Flask web apps
Setup      | Manual engine/session management                  | Simplified setup via Flask config
Syntax     | Verbose, full control                             | Cleaner, Flask-friendly syntax
Ideal For  | Large/custom apps, non-Flask projects             | Flask apps, rapid development

## CONFIGURATION OF FLASK-ALCHEMY
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

## CREATING A MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

## CRUD OPERATIONS
# Create
-Add a new record 
new_user = User(name='John Doe',)
db.session.add(new_user)
db.session.commit()

# Read
-Retrieve data from the database
all_users = User.query.all()
single_
# ****Read***
user = User.query.filter_by(name='John Doe').first()

# Update
-Change an existing record
user.name = 'Jane Doe'
db.session.commit()

# Delete
-Remove a record
# Delete a user
user = User.query.get(1)
if user:
db.session.delete(user)
db.session.commit()
# This code sets up a simple Flask web application with SQLAlchemy support, allowing you to perform CRUD operations on a User model.


## Other flask extensions
- Flask-WTF: For handling forms and CSRF protection.
- Flask-Migrate: For database migrations.
- Flask-Login: For user authentication.
- Flask-Mail: For sending emails.
- Flask-RESTful: For building REST APIs.


## Extra Features in Flask-SQLAlchemy

    Model.query – shorthand for session.query().

    paginate() – built-in support for pagination.

    get_or_404(), first_or_404() – helpful for Flask-based APIs.

## 🔹 Common Config Options

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # avoid overhead