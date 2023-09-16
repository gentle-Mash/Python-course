from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page2")
def generic():
    return render_template("generic.html")

@app.route("/page3")
def elements():
    return render_template("elements.html")


if __name__ == "__main__":
    app.run(debug=True)