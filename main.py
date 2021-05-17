from flask import Flask, render_template, request, redirect
from login import LoginForm

app: Flask = Flask(__name__)
app.config['SECRET_KEY'] = 'bruh'

@app.route("/")
def hello():
    return "Hello Bro"

@app.route("/shell")
def shell():
    return render_template("shell.html")

@app.route("/main")
def main():
    return render_template("main.html", patient="Rajiv")

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        result = request.form
        return render_template('loginres.html', result=result)
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run()