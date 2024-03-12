from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///1-to-many.db"

db = SQLAlchemy()
db.init_app(app)


class Parent(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)
    childs = db.relationship("Child", backref = "parent")

class Child(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    parent_id = db.Column(db.Integer, db.ForeignKey("parent.id"))


with app.app_context():
    db.create_all()

    bazlu = Parent(
        name = "Bazlu",
        address = "123 asd qwe"
    )
    db.session.add(bazlu)
    db.session.commit()

    mahir = Child(
        name = "Mahir",
        age = 22,
        parent = bazlu
    )
    maruf = Child(
        name= "maruf",
        age = 19,
        parent = bazlu

    )
    db.session.add(mahir)
    db.session.add(maruf)
    db.session.commit()

    print(bazlu.childs)
    for childs in bazlu.childs:
        print(childs.name, childs.age)

    print(mahir.parent)
    print(mahir.parent.name, mahir.parent.address)
