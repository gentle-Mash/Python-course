from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = '52a39d2f20c6af3ac5b7a9aa'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-book-collection.db"

db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique = True, nullable = False)
    author = db.Column(db.String(250), nullable = False)
    rating = db.Column(db.Float, nullable = False)

with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/home")
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title = request.form["book_name"],
            author = request.form["author_name"],
            rating = request.form["book_rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book = book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=8000)