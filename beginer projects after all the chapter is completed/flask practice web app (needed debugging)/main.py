from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from addbook import BookForm, Edit

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = '52a39d2f20c6af3ac5b7a9aa'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"

db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
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
    return render_template("index.html", lists=all_books)

@app.route("/add", methods=["GET", 'POST'])
def add():
    register_form = BookForm()
    if register_form.validate_on_submit():
        new_book = {
            "title" : register_form.book.data,
            "author" : register_form.author.data,
            "rating" : register_form.book_rating.data 
        }
        with app.app_context():
            new_book = Book(title=new_book['title'], author=new_book['author'], rating=new_book['rating'])
            db.session.add(new_book)
            db.session.commit()
        
        return redirect(url_for('home'))
    return render_template("add.html", form=register_form)

# @app.route("/edit", methods=["GET", "POST"])
# def edit():
#     update_rating = Edit()
#     book_id = request.args.get('book_id')
#     print(book_id)
#     if update_rating.validate_on_submit():
#         updated_value = update_rating.change_rating.data
#         print(updated_value)
#         book_to_update = db.get_or_404(Book, book_id)
#         book_to_update.rating = updated_value
#         db.session.commit()
#         return redirect(url_for('home'))
    
#     book_selected = db.get_or_404(Book, book_id)
#     return render_template('edit.html', form=update_rating, book=book_selected)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)



if __name__ == "__main__":
    app.run(debug=True, port=8000)