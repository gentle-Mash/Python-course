from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!!!"

@app.route("/<bye>")
def bye(bye):
    return f"{bye + 12}! you people"

@app.route('/username/<yourname>')
def greet(name):
    return f"hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)