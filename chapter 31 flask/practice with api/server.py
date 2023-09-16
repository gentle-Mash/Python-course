from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/")
def home():
    return "it's a demo page"

@app.route("/guess/<name>")
def info(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"
    gender_info = requests.get(gender_url).json()
    age_info = requests.get(age_url).json()

    return render_template("index.html", person_name=name, gender=gender_info["gender"], age=age_info["age"])

if __name__ == "__main__":
    app.run(debug=True)