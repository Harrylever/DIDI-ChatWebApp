from flask import Blueprint, current_app, flash, redirect, render_template, request, session, url_for
import sched, time

views = Blueprint('views', __name__)

messages = []
message_list = []
active_users = []


@views.route('/chathome', methods=['POST', 'GET'])
def chat_home():
    # active_users = []
    if request.method == "POST":
        session.permanent = True
        message_array = request.form['letter']
        message_list.append(message_array)
        session["message"] = message_list
        print(type(session["message"]))
        print(session["message"])
    else:
        if "user" in session and "message" in session:
            user = session["user"]
            if session["user"] not in active_users:
                active_users.append(session["user"])
            messages = session["message"]
            return render_template("pages/index.html", usr=user, msg=messages, act_user=active_users)
        elif "user" in session:
            user = session["user"]
            if session["user"] not in active_users:
                active_users.append(session["user"])
            return render_template("pages/index.html", usr=user, act_user=active_users)
        else:
            # active_users.pop(session["user"])
            return redirect(url_for('auth.login'))
    return render_template("pages/index.html")
