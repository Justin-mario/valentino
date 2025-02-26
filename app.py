from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/about")
def about_us():
    return render_template("about_us.html")

@app.route("/contact")
def contact_us():
    return render_template("contact_us.html")

if __name__ == "__main__":
    app.run(debug=True)