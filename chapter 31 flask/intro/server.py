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


# you can use various types of variables. 
@app.route('/description/<path:name>')
def greet1(name):
    return f"hello {name}!"
# it will take entire path after username as a variable


#you can use different types of variables
@app.route('/username/<name>/<int:number>')
def greet2(name, number):
    return f"hello {name}! you are {number} years old"


# you can also write paths like this
@app.route('/username/<name>/hero')
def greet3(name):
    return f"hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)