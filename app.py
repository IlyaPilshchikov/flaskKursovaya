from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/setka')
def setka():
    return render_template("setka.html")


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/TeamSpirit')
def TeamSpirit():
    return render_template("TeamSpirit.html")


@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)