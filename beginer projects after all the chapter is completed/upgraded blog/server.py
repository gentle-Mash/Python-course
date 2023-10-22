from flask import Flask, render_template, request
import requests, datetime


response = requests.get("https://api.npoint.io/208b68018d663318a066")
blog_list = response.json()


app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template("index.html", posts = blog_list)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/posts/<int:index>")
def post(index):
    return render_template("post.html", blog = blog_list[index-1])

@app.route("/login", methods = ["POST"])
def receive_data():
    name = request.form["username"]
    email = request.form["email"]
    number = request.form["number"]
    message = request.form["message"]
    
    # print(name, email, number, message, end="\n")

    return render_template("contact.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
