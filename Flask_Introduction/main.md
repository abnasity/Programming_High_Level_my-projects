
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
new_user = User(name='John Doe',)
db.session.add(new_user)
db.session.commit()

# Read
user = User.query.filter_by(name='John Doe').first()

# Update
user.name = 'Jane Doe'
db.session.commit()

# Delete
db.session.delete(user)
db.session.commit()




