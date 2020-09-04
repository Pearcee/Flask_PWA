from flask import Flask
from flask import render_template
from datetime import datetime
import re

app = Flask(__name__)


# Replace the existing home function with the one below
@app.route("/")
def home():
    return render_template("home.html")


# New functions
@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route('/offline.html')
def offline():
    return app.send_static_file('offline.html')


@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)