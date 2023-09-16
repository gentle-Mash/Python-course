from flask import Flask

app = Flask(__name__)



@app.route("/")
def html():
    return '<h1 style="color:red"> Hello World </h1> <img src="/city.jpg" width=200>'










if __name__ == "__main__":
    app.run(debug=True)