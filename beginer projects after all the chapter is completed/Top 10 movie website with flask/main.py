from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import requests
from forms import Edit, Add

API_KEY = "1317b92f9abd53cb53c2cdfb52ae4236"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = '52a39d2f20c6af3ac5b7a9aa'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"

db = SQLAlchemy()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/home")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods = ["GET", "POST"])
def edit():
    update_form = Edit()
    movie_id = request.args.get("id")
    movie_selected = db.get_or_404(Movie, movie_id)
    if update_form.validate_on_submit():
        updated_rating = update_form.update_rating.data
        updated_review = update_form.update_review.data
        movie_selected.rating = updated_rating
        movie_selected.review = updated_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form = update_form, movie = movie_selected)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    add_form = Add()
    if add_form.validate_on_submit():
        SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie?"
        MOVIE_TITLE = add_form.movie_title.data
        movie_intro = {
            "api_key" : API_KEY,
            "query" : MOVIE_TITLE
        }
        response = requests.get(SEARCH_ENDPOINT, params=movie_intro)
        response.raise_for_status()
        data = response.json()["results"]
        return render_template("select.html", options = data)
    return render_template("add.html", form = add_form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={
                                "api_key": API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"],
            ranking = 0,
            rating = 0.0,
            review = "None"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))

if __name__ == "__main__":
    app.run(debug=True)


