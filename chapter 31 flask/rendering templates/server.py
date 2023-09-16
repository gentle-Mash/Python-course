from flask import Flask
from flask import render_template


# your html file should be in templates named folder and all your static file like css, images, js shold be in static named folder in your project folder


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug=True)