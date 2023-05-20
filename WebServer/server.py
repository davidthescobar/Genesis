from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<username>/<int:post_id>")
def hello_world(username, post_id):
    return render_template('index.html', name=username, num=post_id)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return "<p>Thoughts about blogs!</p>"