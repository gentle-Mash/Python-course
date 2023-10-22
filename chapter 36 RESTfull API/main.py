from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        # or you could have used dictionary comprehension
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns} 


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    
## HTTP GET - Read Record

# @app.route("/random", methods = ["GET"]) # you could have done it without any methods because GET is by default allowed to all routes

# def random():
#     result = db.session.execute(db.select(Cafe))
#     all_cafes = result.scalars().all()
#     random_cafe = choice(all_cafes)
#     return jsonify(cafe = {
#         "id": random_cafe.id,
#         "name": random_cafe.name,
#         "map_url": random_cafe.map_url,
#         "img_url": random_cafe.img_url,
#         "location": random_cafe.location,
#         "seats": random_cafe.seats,
#         "has_toilet": random_cafe.has_toilet,
#         "has_wifi": random_cafe.has_wifi,
#         "has_sockets": random_cafe.has_sockets,
#         "can_take_calls": random_cafe.can_take_calls,
#         "coffee_price": random_cafe.coffee_price
#     })


#But in most cases, you might just want to return all the data you have on a particular record and it would drive you crazy if you had to write out all that code for every route.

# So another method of serialising our database row Object to JSON is by first converting it to a dictionary and then using jsonify() to convert the dictionary (which is very similar in structure to JSON) to a JSON.

@app.route("/random", methods = ["GET"])
def random():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = choice(all_cafes)
    return jsonify(cafe = random_cafe.to_dict())


@app.route("/all")
def all():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def search():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()

    if all_cafes:
        return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])
    return jsonify(error = {"Not Found" : "Sorry, we don't have a cafe at that location."}), 404


## HTTP POST - Create Record

@app.route("/add", methods = ["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {"success" : "Successfully added the new coffee shop"})


## HTTP PUT/PATCH - Update Record

@app.route("/patch/<int:cafe_id>", methods=['PATCH'])
def patch(cafe_id):
    changed_price = request.args.get("new_price")
    selected_coffee_shop = db.get_or_404(Cafe, cafe_id)

    if selected_coffee_shop:
        selected_coffee_shop.coffee_price = changed_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404



## HTTP DELETE - Delete Record

@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        selected_coffee_shop = db.get_or_404(Cafe, cafe_id)
        if selected_coffee_shop:
            db.session.delete(selected_coffee_shop)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the shop."}), 200
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    return jsonify(error={"Invalid key error":"Wrong API key"}), 403
    
        

if __name__ == '__main__':
    app.run(debug=True)
