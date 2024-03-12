from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///many-to-many.db"

db = SQLAlchemy()
db.init_app(app)


#for many to many relationship, we've to make a third table which is called association table which will associate id's from one table with id's from another table. and by connecting these we'll have a many to many relationship 

user_channel = db.Table("user_channel",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("channel_id", db.Integer, db.ForeignKey("channel.id")))


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    following = db.relationship("Channel", secondary = user_channel, backref = "followers")

    def __repr__(self):
        return f"<User: {self.name}>"    

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"<Channel: {self.name}>"  

with app.app_context():
    db.create_all()

    mashrafi = User(name="Mashrafi")
    jannat = User(name="Jannat")
    benny = Channel(name="Benny Productions")
    pixi = Channel(name = "Piximperfect")

    db.session.add_all([mashrafi, jannat, benny, pixi])
    db.session.commit()


    #now you can imagine this mashrafi.following or jannat.following as lists and use the append method to link up the channels with the users

    mashrafi.following.append(benny)
    mashrafi.following.append(pixi)
    jannat.following.append(pixi)

    db.session.commit()

    print(mashrafi.following)
    for channels in mashrafi.following:
        print(channels.name)

    print(jannat.following)

    print(pixi.followers)
    for users in pixi.followers:
        print(users.name)

    # as it works like a list , you can also use the remove method to unfollow a channel like
    # mashrafi.following.remove(pixi)
    # db.session.commit()