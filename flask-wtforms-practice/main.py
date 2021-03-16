from flask import Flask, render_template
from forms import Login_form
import os






app = Flask(__name__)
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = "some secret string"


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form=Login_form()
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)