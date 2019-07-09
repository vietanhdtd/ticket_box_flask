from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from components.users import users_blueprint
from components.events import events_blueprint
from flask_bootstrap import Bootstrap
from models.ticketbox import db
from models.ticketbox import User
from models.ticketbox import RatingUser





app = Flask(__name__)
db.init_app(app)
migrate = Migrate(app, db , compare_type = True)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


POSTGRES = {
    'user': 'vietanhnguyen',
    'pw': '123',
    'db': 'ticketbox',
    'host': 'localhost',
    'port': '5432'
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'VERY SECRET'
# db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def index():
    return render_template('base.html')


#users
#Handle/users/signUp
#Handle/users/signin
### Old way to do it: 

# @app.route('/users/signup')

#events
#Handle/events/create
#Handle/events/delete


app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(events_blueprint, url_prefix='/events')

if __name__=="__main__":
    app.run(debug=True)
