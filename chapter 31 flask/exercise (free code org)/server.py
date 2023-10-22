from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from registration import Registration


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '2dd2623a342a78e4efa7b321'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    # items = db.relationship("Item", backref="owned_user", lazy=True)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable = False, unique=True)
    price = db.Column(db.Integer(), nullable = False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    # owner = db.Column(db.Integer(), db.ForeignKey("user.id"))

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/pricing")
def pricing():
    items = Item.query.all()
    return render_template("pricing.html", items=items)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("pricing"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            print(f"There was an error creating an user account : {err_msg}")
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)


