from flask import Flask, render_template, request
from connect_db import db

app = Flask(__name__)

from routes import routes

if __name__ == "__main__":
    app.run(debug=True)