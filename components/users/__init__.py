from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from components.users.forms.forms import SignupForm, LoginForm, EmailForm
from models.ticketbox import User
from models.ticketbox import db
from flask_login import logout_user, login_user
from itsdangerous import URLSafeTimedSerializer
import requests
#Define blueprint
users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/register', methods = ['POST', 'GET'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data,
                        name = form.name.data,
                        email = form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("users.login"))
    return render_template('register.html', form = form)

@users_blueprint.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        log_user = User.query.filter_by(username = form.username.data).first()
        if log_user is None: 
            flash("Your username doesn't exist")
            return redirect(url_for('users.login'))
        if not log_user.check_password(form.password.data):
            flash("Incorrect password")
            return render_template('login.html', form = form)
        flash("Login Success")
        login_user(log_user)
        return redirect(url_for('events.feeds'))
    return render_template("login.html", form = form)

@users_blueprint.route('/<int:user_id>/profile')
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    return render_template('profile.html', user = user)


@users_blueprint.route('/logout')
def logout():
    logout_user()
    flash("Logout Success")
    return redirect(url_for('events.feeds'))


@users_blueprint.route('/reset', methods =['get','post'])
def reset_password():
    form = EmailForm()
    if form.validate_on_submit():
        #POST
        #validate email
        try:
            User.query.filter_by(email = form.email.data).first_or_404()
        except:
            flash("Invalid email address!!",'warning')
            return redirect(url_for("users.reset_password"))
        #CREATE TOKEN 
        ts = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        token = ts.dumps(form.email.data, salt = 'password_reset_salt')
        print('token: ', token)
        #send token to email
        send_email("Reset password", form.email.data, token)

    #GET
    return render_template('reset.html', form = form)

MAILGUN_API_KEY ='4dc8472f0363af2cf4ee57254f22bd3b-afab6073-a8ce30d5'
MAILGUN_DOMAIN_NAME ='sandbox89a2755158564cffb77a2922b44be07c.mailgun.org'

def send_email(title, email, html):
    url = 'https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN_NAME)
    auth = ('api', MAILGUN_API_KEY)
    data = {
        'from': 'Mailgun User <mailgun@{}>'.format(MAILGUN_DOMAIN_NAME),
        'to': email,
        'subject': title,
        'text': 'Plaintext content',
        'html': html
    }
    response = requests.post(url, auth=auth, data=data)
    response.raise_for_status()

@users_blueprint.route('reset_token/<token>', methods = ['get', 'post'])
def reset_with_token(token):
    pass