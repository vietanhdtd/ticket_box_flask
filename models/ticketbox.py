
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class RatingUser(db.Model):
    __tablename__='rating_users'
    rater_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    target_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    buyer_id = db.relationship('Purchase', backref = 'buyer', lazy = True)
    event = db.relationship('Event', backref = 'owner', lazy = True)
    rater_id = db.relationship('RatingUser', primaryjoin=(id==RatingUser.rater_id))
    target_user_id = db.relationship('RatingUser', primaryjoin=(id==RatingUser.target_user_id))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255), nullable = False)
    location = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(4000), nullable = False)
    starting_date = db.Column(db.DateTime)
    image_url = db.Column(db.String(500), nullable = False)
    date_create = db.Column(db.DateTime, server_default = db.func.now())

    ticket_type = db.relationship('Ticket', backref = 'event', lazy = True)

class Purchase(db.Model):
    __tablename__ = 'purchase'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    quantity = db.Column(db.Integer, nullable = False)
    date_purchase = db.Column(db.DateTime, server_default = db.func.now())
    payment_menthod = db.Column(db.String(255), nullable = False)
    ticket_type = db.Column(db.Integer, db.ForeignKey('tickets.id'))

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key = True)
    ticket_name = db.Column(db.String(255), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    purchase_id = db.relationship('Purchase', backref = 'purchase_ticket', lazy = True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

# class RatingUser(db.Model):
#     __tablename__='rating_users'
#     rater_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
#     target_user_id = db.Column( db.Integer, db.ForeignKey('users.id'), primary_key = True)
#     rating = db.Column( db.Integer, nullable = False)

# class User(db.Model, UserMixin):
#     __tablename__='users'
#     id = db.Column(db.Integer, primary_key = True)	  
#     username = db.Column(db.String(80), nullable = False, unique = True)	  
#     name = 	db.Column(db.String(255), nullable = False)	  
#     email = db.Column(db.String(255), nullable = False, unique = True)	  
#     password = db.Column(db.String(255), nullable = False)
#     rater_id = db.relationship('users', 
#         secondary = rating_users, backref = db.backref('target_user_id'),
#         primaryjoin = (rating_users.c.rater_id == id), # self many many
#         secondaryjoin = (rating_users.c.target_user_id == id),
#         lazy = 'subquery',
#         backref = db.backref('target_user_id', lazy = True)
#         )


