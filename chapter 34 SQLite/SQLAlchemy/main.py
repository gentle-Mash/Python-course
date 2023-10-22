from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#create Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

#create extension
db = SQLAlchemy()

#initialise the app with the extension
db.init_app(app)

#create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique = True, nullable = False)
    author = db.Column(db.String(250), nullable = False)
    rating = db.Column(db.Float, nullable = False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

#create record
with app.app_context():
    new_book = Book(title="The caring Husband", author="Jannat Begum", rating=5.0)
    db.session.add(new_book)
    db.session.commit()

# print(new_book.__repr__)

#read all records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books)

# read a particular record
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    print(book)

# update a particular record by query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()
    print(book_to_update.title)

# update a record by primary key
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    # or you can also do this
    # book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of fire"
    db.session.commit()
    print(book_to_update.title)

# Delete a particular record by primary key
with app.app_context():
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
