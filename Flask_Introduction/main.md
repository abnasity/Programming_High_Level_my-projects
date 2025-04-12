
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
