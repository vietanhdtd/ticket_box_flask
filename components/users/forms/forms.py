
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email
from models.ticketbox import User


class SignupForm(FlaskForm):
    username = StringField('User name', validators = [InputRequired()]) 
    name = StringField('Name', validators = [InputRequired()]) 
    email =  StringField(' Email', validators = [InputRequired()])
    password = PasswordField(' Password', validators = [InputRequired()])
    submit = SubmitField('Sign Up')

    def __repr__(self):
        return "<User {}>".format(self.username)

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Your email has been registered!")

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Your username has been registered")

class LoginForm(FlaskForm):
    username = StringField('User name', validators = [InputRequired()])
    password = PasswordField(' Password', validators = [InputRequired()])
    submit = SubmitField('Sign Up')

class EmailForm(FlaskForm):
    email = StringField("Email", validators = [InputRequired(), Email()])
    submit = SubmitField("Submit")
