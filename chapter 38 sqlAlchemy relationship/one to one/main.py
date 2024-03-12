from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///1-to-1.db"

db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), nullable = False)
    profile = db.relationship("Profile", backref = "user", uselist = False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique = True)


with app.app_context():
    db.create_all()

    mashrafi_email = User(email="mashrafi@mail.com")
    mashrafi_name = Profile(name="Mashrafi", user = mashrafi_email)
    jannat_email = User(email = "jannat@mail.com")
    jannat_name = Profile(name = "Jannat", user =jannat_email)

    db.session.add_all([mashrafi_email, mashrafi_name,jannat_email,jannat_name])
    db.session.commit()

