from server import app, db, Item, User

app.app_context().push()
db.drop_all()
db.create_all()

user1 = User(username="deku", email="deku@mail.com", password_hash="hfi43tuqt4")

item1 = Item(name="Iphone 10", price=99900, barcode="123456789102", description="desc")

db.session.add(item1)
db.session.add(user1)
db.session.commit()