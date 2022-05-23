from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

# data (/data )
# about us
@app.route("/data")
def data():
    return "Something"

@app.route("/about_us")
def about_us():
    return "Website under construction"