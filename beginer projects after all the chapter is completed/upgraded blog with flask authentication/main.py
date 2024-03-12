from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from forms import CreatePostForm, CreateRegistrationForm, LoginForm, CommentForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)
# TODO: Configure Flask-Login

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)



# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


def admin_only(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if (not current_user.id == 1) or (not current_user.is_authenticated):
            return abort(403)
        return f(*args, **kwargs)
    return decorator

# CONFIGURE TABLES
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    password = db.Column(db.String, nullable = False)
    posts = db.relationship("BlogPost", backref = "author" )
    comments = db.relationship("Comment", backref = "commenter")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    # author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    comments = db.relationship("Comment", backref = "the_blog")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text, nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))


# TODO: Create a User table for all your registered users. 


with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods = ["GET", "POST"])
def register():
    form = CreateRegistrationForm()
    if form.validate_on_submit():
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            flash("There is already an account with that email, try login instead")
            return redirect(url_for('login'))
        new_user = User(
            name = form.name.data,
            email = form.email.data,
            password = generate_password_hash(password=form.password2.data, method="pbkdf2:sha256:600000", salt_length=16)
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form, current_user=current_user)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()

        if not user:
            flash("This email doesn't exists, try again")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, form.password.data):
            flash("Incorrect Password. try again")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))



@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods = ["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("you need to login or register to comment.")
            return redirect(url_for('login'))
        
        new_comment = Comment(
            comment = form.comment.data,
            commenter = current_user,
            the_blog = db.get_or_404(BlogPost, post_id)
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post,form=form, current_user=current_user)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author.name,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=True)
