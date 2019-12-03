# Import dependencies
from flask import Flask, render_template

# Create instance of Flask App
app = Flask(__name__)


# Define Route
@app.route("/")
# Content
def home():
    return "Home Page"


# Define 2nd Route and Content
@app.route("/about")
def about():
    return "About Me"


@app.route("/blog")
def blog():
    return render_template("blog.html")


# Running and Controlling the script
if __name__ == "__main__":
    app.run(debug=True)


