from flask import Flask, render_template
import requests
from post import Post


response = requests.get("https://api.npoint.io/baf85e335dddd6839b77").json()
blog_posts = []
for blogs in response:
    blog_obj = Post(blogs["id"], blogs["title"], blogs["subtitle"], blogs["body"])
    blog_posts.append(blog_obj)

app = Flask(__name__)

@app.route('/')
def home():

    json_data = requests.get("https://api.npoint.io/baf85e335dddd6839b77").json()
    return render_template("index.html", blog_posts = json_data)

@app.route("/post/<int:index>")
def main_post(index):
    requested_post = None
    for posts in blog_posts:
        if posts.id == index:
            requested_post = posts
            return render_template("post.html", post= requested_post)

if __name__ == "__main__":
    app.run(debug=True)
