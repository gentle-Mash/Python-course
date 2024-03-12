from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from datetime import date
from forms import NewPost



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
@app.route("/home")
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.id))
    all_posts = result.scalars().all()
    # posts = []
    return render_template("index.html", all_posts=all_posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/show_post')
def show_post():
    # TODO: Retrieve a BlogPost from the database based on the post_id
    post_id = request.args.get("post_id")
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new_post", methods=["GET","POST"])
def add_new_post():
    post_form = NewPost()
    if post_form.validate_on_submit():
        new_post = BlogPost(
            title=post_form.title.data,
            subtitle=post_form.subtitle.data,
            body=post_form.body.data,
            img_url=post_form.img_url.data,
            author=post_form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=post_form)

# TODO: edit_post() to change an existing blog post

@app.route("/edit", methods=["GET", "POST"])
def edit():
    post_id = request.args.get("post")
    post_need_to_edit = db.get_or_404(BlogPost, post_id)
    edit_form = NewPost(
        title = post_need_to_edit.title,
        subtitle = post_need_to_edit.subtitle,
        img_url = post_need_to_edit.img_url,
        author = post_need_to_edit.author,
        body = post_need_to_edit.body,

    )
    if edit_form.validate_on_submit():
        
        post_need_to_edit.title=edit_form.title.data
        post_need_to_edit.subtitle=edit_form.subtitle.data
        post_need_to_edit.body=edit_form.body.data
        post_need_to_edit.img_url=edit_form.img_url.data
        post_need_to_edit.author=edit_form.author.data
    
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: delete_post() to remove a blog post from the database

@app.route("/delete")
def delete():
    post_id = request.args.get("post")
    delete_post = db.get_or_404(BlogPost, post_id)
    db.session.delete(delete_post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
