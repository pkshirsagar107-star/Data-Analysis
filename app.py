from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

app.run(debug=True)

@app.route("/about")
def about():
    return "About Page"

app.run(debug=True)