from flask import Flask, render_template, redirect, url_for
from registration import Registration
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = '2dd2623a342a78e4efa7b321'
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/denied")
def denied():
    render_template("denied.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Registration()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com":
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template("login.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration()
    form.validate_on_submit()
    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
