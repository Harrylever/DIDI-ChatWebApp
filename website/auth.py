from flask import Blueprint, redirect, render_template, request, flash, session, url_for
# import 

auth = Blueprint('auth', __name__)

@auth.route('/')
def redirect_from_home():
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['username']
        session["user"] = user
        return redirect(url_for("views.chat_home"))
    else:
        if "user" in session:
            return redirect(url_for("views.chat_home"))

        return render_template("pages/login.html")


@auth.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for('auth.login'))