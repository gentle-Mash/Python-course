# here is a problem , if we change anything in our code, the change won't be shown in our server. means it won't change in live server. for the change to be shown we have to quit the server and re run our code, but it's a hassle to us. to avoid this hassle we have to turn the debugger mode on.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!!!"

@app.route("/bye")
def bye():
    return "bye! you people"

@app.route('/username/<name>')
def greet(name):
    return f"hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)