from flask import Blueprint,render_template

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/sign-up')
def SignUp():
    return render_template("sign_up.html")

@auth.route('/logout')
def logout():
    return "<h1>logout successful </h1>"
