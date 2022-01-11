from flask import Flask, render_template
from post import Post
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(url=blog_url).json()
post_objects = []
for each_post in posts:
    post_obj = Post(each_post["id"], each_post["title"], each_post["subtitle"], each_post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    return render_template("post.html", all_posts=post_objects, post_index=index)


if __name__ == "__main__":
    app.run(debug=True)
