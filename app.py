from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def index():
    return render_template("new.html")

@app.route("/show")
def index():
    return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)